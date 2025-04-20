from models import SchedulerOutput

def show_schedule(output: SchedulerOutput):
    print("\n📆 Your Personalized Study Plan:\n")
    for day in output.daily_schedule:
        print(f"{day.day}:")
        for block in day.study_blocks:
            print(f"  - {block.subject} ({block.duration}h)")
    print(f"\n🧠 Total Study Time: {output.total_study_time}h")
    print(f"✅ Valid: {output.validation_passed}")
    print(f"📝 Notes: {output.notes}")
    print("\n🧾 Reasoning:\n" + output.reasoning)
