from perception import analyze_query
from decision import generate_study_plan
from action import write_to_google_sheet, send_email
from memory import remember_query

# Step 1: Simulated user query
user_query = "Make a weekly study plan for Science and Math for my 8th-grade exams. " \
             "Save it to a Google Sheet and email it to me."
telegram_chat_id = 2    # Simulated chat ID
# Step 2: Perception layer
request = analyze_query(user_query, telegram_chat_id)
print("\nParsed StudyPlanRequest:")
print(request)

# Step 3: Decision layer
study_plan = generate_study_plan(request)
print("\nGenerated Study Plan:")
print(study_plan)

# Step 4: Action layer - Write to Google Sheet
sheet_url = write_to_google_sheet(study_plan, request.email)
print("\n✅ Study Plan saved to Google Sheet:", sheet_url)

# Step 5: Action layer - Send email
send_email(to=request.email, link=sheet_url)

# Step 6: Memory - Store the interaction
remember_query(user_query, study_plan.summary)

print("\n🎉 End-to-end test completed successfully!")
