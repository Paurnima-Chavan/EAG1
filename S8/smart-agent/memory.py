import json
from typing import List, Optional
from models import StudyPlanRequest, StudyPlanOutput
import datetime

# In-memory list for now (you can replace with persistent store)
past_study_plans: List[dict] = []

LOG_FILE = "memory_log.txt"

def remember_query(user_text: str, summary: str):
    """Store the user query and summary with timestamp into a local file."""
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "query": user_text,
        "summary": summary
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print("🧠 Memory updated.")


def save_study_plan(request: StudyPlanRequest, output: StudyPlanOutput):
    """
    Save a generated study plan to memory for audit/history/logging.
    """
    entry = {
        "user_email": request.user_email,
        "chat_id": request.telegram_chat_id,
        "subjects": request.study_input.subjects,
        "grade_level": request.study_input.grade_level,
        "preference": request.study_input.preference,
        "schedule": output.schedule,
        "notes": output.notes,
        "sheet_url": output.sheet_url
    }
    past_study_plans.append(entry)


def get_latest_plan_for_user(chat_id: int) -> Optional[dict]:
    """
    Retrieve the most recent study plan for a given Telegram user.
    """
    for plan in reversed(past_study_plans):
        if plan["chat_id"] == chat_id:
            return plan
    return None


def export_memory_to_json(file_path="memory_backup.json"):
    """
    Optionally, export the stored memory to a JSON file.
    """
    with open(file_path, "w") as f:
        json.dump(past_study_plans, f, indent=2)
