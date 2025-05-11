from fastapi import UploadFile
from pydantic import BaseModel
import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

from action import get_gsheet_client

# Load credentials
SERVICE_ACCOUNT_FILE = os.getenv("GDRIVE_CREDENTIALS_FILE", r"C:\TFS\other\EAG1\S8\smart-agent\credentials.json")
SCOPES = ['https://www.googleapis.com/auth/drive.file']


def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)


def upload_file_to_drive(file_name: str, file_content: str, mime_type: str = "text/plain") -> str:
    """
    Uploads a file to Google Drive and returns the public link.
    """
    print(SERVICE_ACCOUNT_FILE)
    drive_service = get_drive_service()
    file_metadata = {'name': file_name}
    media = MediaIoBaseUpload(io.BytesIO(file_content.encode()), mimetype=mime_type)

    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    file_id = uploaded_file.get('id')

    # Make file publicly viewable
    drive_service.permissions().create(
        fileId=file_id,
        body={'role': 'reader', 'type': 'anyone'},
    ).execute()

    public_url = f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"
    return public_url


def create_google_sheet(title: str, rows: list[list[str]], email: str) -> str:
    client = get_gsheet_client()
    sheet = client.create(title)
    worksheet = sheet.get_worksheet(0)
    worksheet.update("A1", rows)  # Bulk insert all rows starting at A1

    # Share the sheet
    sheet.share(email, perm_type="user", role="writer")
    return sheet.url
