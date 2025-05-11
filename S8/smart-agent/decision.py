import asyncio
import json

from models import StudyPlanRequest, StudyPlanOutput, StudyBlock, StudyPreferences, DailySchedule
from core.session import MultiMCP

# Define tool script mappings
MCP_SERVERS = [
    {"script": "mcp_servers/mcp_server_4_study_plan.py"},
    {"script": "mcp_servers/mcp_server_7_telegram_notify.py"}
]

# Initialize MCP client once (you can move this to context.py for reuse)
mcp = MultiMCP(MCP_SERVERS)


async def generate_study_plan_async(request: StudyPlanRequest) -> StudyPlanOutput:

    await mcp.initialize()

    preferences = StudyPreferences(
        subjects=request.subjects,
        available_hours_per_day=sum(request.availability.values()) // 7,
        prefers_evening=request.prefers_evening,
        telegram_chat_id=request.telegram_chat_id,
        prefers_morning=request.prefers_morning
    )

    result = await mcp.call_tool("generate_study_plan", arguments={"preferences": preferences.dict()})
    raw_output = result.content[0].text  # This is a JSON string
    parsed = json.loads(raw_output)  # Convert to Python dict
    # ✅ Access attributes of result directly
    weekly_schedule = {}

    for block in parsed["plan"]:
        day = block["day"]
        if day not in weekly_schedule:
            weekly_schedule[day] = []

        weekly_schedule[day].append({
            "subject": block["subject"],
            "hours": str(block["duration_minutes"] / 60)
        })

    summary = f"Generated plan using MCP tool for subjects: {', '.join(preferences.subjects)}"
    return StudyPlanOutput(weekly_schedule=weekly_schedule, summary=summary)


# For backward compatibility
def generate_study_plan(request: StudyPlanRequest) -> StudyPlanOutput:
    return asyncio.run(generate_study_plan_async(request))
