import streamlit as st
import json
from scheduler import generate_study_schedule

st.title("📚 Smart Study Scheduler")

subjects = st.text_area("Subjects (JSON List)", value=json.dumps([
    {"name": "Math", "difficulty": 5, "exam_date": "2025-05-01"},
    {"name": "History", "difficulty": 2, "exam_date": "2025-05-15"},
    {"name": "Physics", "difficulty": 4, "exam_date": "2025-05-05"}
], indent=2))

availability = st.text_area("Weekly Availability (JSON Dict)", value=json.dumps({
    "Monday": 3, "Tuesday": 4, "Wednesday": 4,
    "Thursday": 3, "Friday": 2, "Saturday": 6, "Sunday": 6
}, indent=2))

if st.button("Generate Schedule"):
    try:
        input_data = {
            "subjects": json.loads(subjects),
            "weekly_availability": json.loads(availability)
        }
        result = generate_study_schedule(input_data)
        st.json(result)
    except Exception as e:
        st.error(f"Error: {e}")
