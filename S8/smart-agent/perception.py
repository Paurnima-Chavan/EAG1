from models import StudyPlanRequest, StudyPlanInput
from typing import Optional
import re


def analyze_query(text: str, telegram_chat_id: str,
                  user_email: str = "paurnimach@gmail.com") -> Optional[StudyPlanRequest]:
    """
    Parses a natural language query and returns a structured StudyPlanRequest.
    """

    text = text.lower()

    # Extract subjects from query
    subjects = []
    for subject in ["math", "science", "history", "english"]:
        if subject in text:
            subjects.append(subject.capitalize())

    if not subjects:
        subjects = ["Math", "Science"]  # default fallback

    # Extract grade level
    grade_level = "8th Grade"
    match = re.search(r'(\d+)(st|nd|rd|th)[ -]?grade', text)
    if match:
        grade_level = f"{match.group(1)}th Grade"

    # Extract preference if mentioned
    preference = None
    if "focus on science" in text:
        preference = "Focus more on Science"
    elif "focus on math" in text:
        preference = "Focus more on Math"

    # Preference time of day
    prefers_evening = "evening" in text
    prefers_morning = "morning" in text

    # Set basic default availability
    available_hours = {
        "Monday": 1,
        "Tuesday": 1,
        "Wednesday": 1,
        "Thursday": 1,
        "Friday": 1,
        "Saturday": 2,
        "Sunday": 2,
    }

    # Build the final request
    return StudyPlanRequest(
        subjects=subjects,
        grade_level=grade_level,
        availability=available_hours,
        email=user_email,
        prefers_evening=prefers_evening,
        prefers_morning=prefers_morning,
        telegram_chat_id=telegram_chat_id,
        preference=preference
    )

