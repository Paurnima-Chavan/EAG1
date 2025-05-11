from fastapi import APIRouter
from sse_server.utils.drive_utils import  create_google_sheet
from pydantic import BaseModel


router = APIRouter(prefix="/tools")


class StudyPlanUploadRequest(BaseModel):
    title: str
    rows: list[list[str]]  # List of rows as lists of strings
    email: str


@router.post("/upload_study_plan")
@router.post("")
def upload_study_plan(request: StudyPlanUploadRequest):
    print("Received upload request:", request)
    sheet_url = create_google_sheet(request.title, request.rows, request.email)
    print(sheet_url)
    return {"status": "success", "sheet_url": sheet_url}

