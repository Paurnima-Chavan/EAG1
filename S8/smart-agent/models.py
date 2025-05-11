from pydantic import BaseModel
from typing import List, Optional, Dict

class StudyPreferences(BaseModel):
    subjects: List[str]
    available_hours_per_day: int = 2
    prefers_evening: Optional[bool] = False
    prefers_morning: Optional[bool] = False


class StudyBlock(BaseModel):
    subject: str
    duration_minutes: int
    day: str
    time: str


class StudyPlan(BaseModel):
    total_blocks: int
    plan: List[StudyBlock]


class StudyPlanInput(BaseModel):
    grade_level: str  # e.g., "8th Grade"
    subjects: List[str]  # e.g., ["Science", "Math"]
    exams_coming_up: bool = True
    preference: Optional[str] = None  # e.g., "Focus more on Science"


class StudyPlanOutput(BaseModel):
    weekly_schedule: Dict[str, List[Dict[str, str]]]
    summary: str


class StudyPlanRequest(BaseModel):
    subjects: List[str]
    grade_level: str
    availability: Dict[str, int]
    email: str
    prefers_evening: bool = False
    prefers_morning: bool = False
    telegram_chat_id: Optional[str] = None


class DailySchedule(BaseModel):
    subject: str
    hours: int
