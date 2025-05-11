from perception import analyze_query
from decision import generate_study_plan_async
from action import write_to_google_sheet, send_email, call_drive_sse_upload
from memory import remember_query
from models import StudyPlanRequest, StudyPlanOutput
import asyncio


async def run_agent(user_text: str) -> str:
    # 1. Perception: Understand the user's request
    print("🔍 Analyzing query...")
    request: StudyPlanRequest = analyze_query(user_text, telegram_chat_id="2")
    print(f"🎯 Parsed Request: Subjects={request.subjects}, Grade={request.grade_level}, Email={request.email}")

    # 2. Decision: Call MCP tool to generate study plan
    print("🧠 Generating study plan using MCP tool...")
    plan: StudyPlanOutput = await generate_study_plan_async(request)

    # 3. Memory: Log the request
    remember_query(user_text, plan.summary)

    # 4. Action: Write the plan to Google Sheets
    print("📄 Writing to Google Sheets...")
    # sheet_link = write_to_google_sheet(plan, request.email)
    sheet_link = call_drive_sse_upload(plan, request.email)
    print(f"✅ Google Sheet created: {sheet_link}")

    # 5. Action: Email the link to the user
    print("📧 Sending email...")
    send_email(request.email, sheet_link)

    return f"Study plan sent to {request.email}. Link: {sheet_link}"


# Allow testing standalone
if __name__ == "__main__":
    query = "Make a weekly study plan for Science and Math for my 8th-grade exams. " \
            "Save it to a Google Sheet and email it to me."
    result = asyncio.run(run_agent(query))
    print(result)
