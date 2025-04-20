import json
from scheduler import generate_study_schedule

if __name__ == "__main__":
    with open("sample_input.json") as f:
        user_input = json.load(f)

    result = generate_study_schedule(user_input)
    print(json.dumps(result, indent=2))
