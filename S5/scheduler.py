import openai
import os

from gpt_caller import GPTCaller
from prompts import build_prompt
from validator import validate_output
import re
import json

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_study_schedule(user_input):
    prompt = build_prompt(user_input)
    gpt_caller = GPTCaller()

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a helpful study planner."},
            {"role": "user", "content": prompt}
        ],

    )

    raw_output = response.choices[0].message.content
    json_output = extract_json_from_response(raw_output)

    if "error" in json_output:
        return json_output

    validated_output = validate_output(json_output)
    return validated_output


# Function to extract JSON from the raw output
def extract_json_from_response(raw_output):
    try:
        # Use regex to extract JSON block between first "{" and last "}"
        match = re.search(r'\{.*\}', raw_output, re.DOTALL)
        if not match:
            return {"error": "No JSON object found in response."}

        json_str = match.group(0)

        # Now try to load it safely using json.loads
        json_output = json.loads(json_str)
        return json_output

    except json.JSONDecodeError as e:
        return {"error": "Failed to parse JSON", "details": str(e)}
