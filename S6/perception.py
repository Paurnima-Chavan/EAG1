

def collect_user_input():
    print("🎯 Let's gather your study preferences.")

    preferred_subject = input("Which subject do you enjoy most? ")
    learning_style = input("Your preferred learning style (visual/auditory/practice-heavy)? ")

    subjects = [
        {"name": "Math", "difficulty": 5, "exam_date": "2025-05-01"},
        {"name": "Physics", "difficulty": 4, "exam_date": "2025-05-05"},
        {"name": "History", "difficulty": 2, "exam_date": "2025-05-15"}
    ]

    availability = {
        "Monday": 3, "Tuesday": 4, "Wednesday": 4,
        "Thursday": 3, "Friday": 2, "Saturday": 6, "Sunday": 6
    }

    return {
        "subjects": subjects,
        "availability": {"daily_hours": availability},
        "preferences": {
            "preferred_subject": preferred_subject,
            "learning_style": learning_style
        }
    }
