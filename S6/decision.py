import openai
import os
import json
import re

from gpt_caller import GPTCaller
from models import UserInput, SchedulerOutput

openai.api_key = os.getenv("OPENAI_API_KEY")


def build_schedule(user_data: UserInput) -> SchedulerOutput:
    prompt = f"""
You are a helpful study planning assistant.

User Preferences:
- Favorite subject: {user_data.preferences.preferred_subject}
- Learning style: {user_data.preferences.learning_style}

Subjects:
{user_data.subjects}

Weekly Availability (hours per day):
{user_data.availability.daily_hours}

Task:
Plan a 7-day study schedule that:
- Prioritizes more difficult subjects
- Gives more time to earlier exams
- Fits within the daily available hours
- Takes into account learning style
- Outputs a valid JSON structure like this:

{{
  "daily_schedule": [
    {{
      "day": "Monday",
      "study_blocks": [
        {{"subject": "Math", "duration": 2}},
        ...
      ]
    }},
    ...
  ],
  "total_study_time": 28,
  "validation_passed": true,
  "reasoning": "How the plan was built",
  "notes": "Summary of choices made"
}}

Please reason step-by-step and output only the JSON.
"""
    gpt_caller = GPTCaller()
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "You are a structured, logic-based planner."},
    #         {"role": "user", "content": prompt}
    #     ],
    #     temperature=0.4
    # )
    messages = [
        {"role": "system", "content": "You are a structured, logic-based planner."},
        {"role": "user", "content": prompt}
    ]
    response = gpt_caller.query_gpt(messages)

    content = response.choices[0].message.content
    json_str = re.search(r'\{.*\}', content, re.DOTALL).group()
    return SchedulerOutput.model_validate(json.loads(json_str))
