import aiosmtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = os.getenv("GMAIL_USER")
SENDER_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


async def send_email_sse(to: str, subject: str, body: str):
    message = MIMEText(body)
    message["From"] = SENDER_EMAIL
    message["To"] = to
    message["Subject"] = subject

    try:
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            username=SENDER_EMAIL,
            password=SENDER_PASSWORD,
            use_tls=True,
        )
        return {"status": "success", "detail": f"Email sent to {to}"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
