
# This script defines a function to build a prompt for a study plan generator agent.
def build_prompt(user_input):
    return f"""
You are a Study Plan Generator Agent. Create a 7-day schedule in the following strict format.

Example Output Format (use exactly this):

{{
  "daily_schedule": [
    {{
      "day": "Monday",
      "study_blocks": [
        {{ "subject": "Math", "duration": 2 }},
        {{ "subject": "Physics", "duration": 1 }}
      ]
    }},
    ...
  ],
  "total_study_time": 28,
  "validation_passed": true,
  "notes": "Explain how time was allocated."
}}

Only output valid JSON. Do not add explanations or text before/after.
Now use the following data:
Subjects:
{user_input['subjects']}
Availability:
{user_input['weekly_availability']}
"""
