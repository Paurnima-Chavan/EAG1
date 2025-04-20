# 📚 Smart Study Scheduler

An AI-powered plugin that builds a personalized 7-day study schedule based on your subjects, difficulty, and availability. Designed using structured prompting, validation steps, and fallback handling.

## 🧠 How It Works

1. Accepts:
   - List of subjects
   - Difficulty (1–5)
   - Weekly availability
   - Exam dates (optional)

2. Outputs:
   - Day-by-day plan
   - Total hours per subject
   - Validation summary
   - Notes on fallback if needed

## 📦 Features

✅ Step-by-step CoT reasoning  
✅ Structured JSON output  
✅ Self-checking logic  
✅ Error fallback for time constraints  

## 📥 Input Example

```json
{
  "subjects": [
    {"name": "Math", "difficulty": 5, "exam_date": "2025-05-01"},
    {"name": "History", "difficulty": 2, "exam_date": "2025-05-15"},
    {"name": "Physics", "difficulty": 4, "exam_date": "2025-05-05"}
  ],
  "weekly_availability": {
    "Monday": 3,
    "Tuesday": 4,
    "Wednesday": 4,
    "Thursday": 3,
    "Friday": 2,
    "Saturday": 6,
    "Sunday": 6
  }
}
