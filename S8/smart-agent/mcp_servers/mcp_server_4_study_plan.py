from mcp.server.fastmcp import FastMCP
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import StudyPreferences, StudyPlan, StudyBlock
import random

mcp = FastMCP("StudyPlanServer")

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


@mcp.tool()
def generate_study_plan(preferences: StudyPreferences) -> StudyPlan:
    blocks = []
    total_minutes = preferences.available_hours_per_day * 60
    subjects = preferences.subjects
    daily_minutes = total_minutes // len(subjects)
    study_time = "18:00" if preferences.prefers_evening else "09:00"
    random.shuffle(DAYS)

    for i, subject in enumerate(subjects):
        for j in range(3):  # 3 sessions per subject
            day = DAYS[(i + j) % len(DAYS)]
            blocks.append(StudyBlock(subject=subject, duration_minutes=daily_minutes, day=day, time=study_time))

    return StudyPlan(total_blocks=len(blocks), plan=blocks)


if __name__ == "__main__":
    mcp.run(transport="stdio")
