import os
from typing import Dict
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.text import MIMEText
from models import StudyPlanOutput
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()


# Authenticate with Google Sheets using credentials.json
def get_gsheet_client():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    cred_path = os.path.join(os.path.dirname(__file__), "credentials.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scope)
    return gspread.authorize(creds)


# Write study plan to Google Sheet and return the shareable link
def write_to_google_sheet(plan: StudyPlanOutput, email: str) -> str:
    client = get_gsheet_client()
    sheet = client.create("Weekly Study Plan")

    # Share sheet with user's Gmail
    sheet.share(email, perm_type="user", role="writer")

    worksheet = sheet.get_worksheet(0)
    worksheet.update_title("Study Schedule")
    worksheet.append_row(["Day", "Subject", "Hours"])

    for day, items in plan.weekly_schedule.items():
        for entry in items:
            worksheet.append_row([day, entry.get("subject"), entry.get("hours")])

    return sheet.url


def call_drive_sse_upload(plan, email: str) -> str:
    rows = [["Day", "Subject", "Hours"]]
    for day, items in plan.weekly_schedule.items():
        for entry in items:
            rows.append([day, entry.get('subject'), str(entry.get('hours'))])

    payload = {
        "title": "Weekly Study Plan",
        "rows": rows,
        "email": email
    }
    response = requests.post("http://localhost:8000/tools/upload_study_plan", json=payload)
    print("Status Code:", response.status_code)
    # print("Response Text:", response.text)
    response_data = response.json()
    return response_data.get("sheet_url", "Upload succeeded but no link returned")


def serialize_study_plan_to_markdown(plan: StudyPlanOutput) -> str:
    markdown = "# Weekly Study Plan\n\n"
    for day, entries in plan.weekly_schedule.items():
        markdown += f"## {day}\n"
        for entry in entries:
            markdown += f"- **{entry.get('subject')}**: {entry.get('hours')} hour(s)\n"
    markdown += f"\n---\n\n**Summary**: {plan.summary}\n"
    return markdown


# Email the sheet link to user
def send_email(to: str, link: str):
    sender = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_APP_PASSWORD")

    message = MIMEText(
        f"""
Hi,

Your weekly study plan is ready and saved to Google Sheets!

📄 Access it here: {link}

Best of luck with your studies!
– Smart Study Agent
""")
    message["Subject"] = "📚 Your Study Plan is Ready"
    message["From"] = sender
    message["To"] = to

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(message)
        print(f"Email sent to {to}")
