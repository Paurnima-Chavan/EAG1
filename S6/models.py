from pydantic import BaseModel, Field
from typing import List, Dict


class Subject(BaseModel):
    name: str
    difficulty: int = Field(ge=1, le=5)
    exam_date: str


class Availability(BaseModel):
    daily_hours: Dict[str, int]  # {"Monday": 3, ...}


class Preferences(BaseModel):
    preferred_subject: str
    learning_style: str  # visual / auditory / practice-heavy


class UserInput(BaseModel):
    subjects: List[Subject]
    availability: Availability
    preferences: Preferences


class StudyBlock(BaseModel):
    subject: str
    duration: int


class DailyPlan(BaseModel):
    day: str
    study_blocks: List[StudyBlock]


class SchedulerOutput(BaseModel):
    daily_schedule: List[DailyPlan]
    total_study_time: int
    validation_passed: bool
    reasoning: str
    notes: str
