def validate_output(output):
    required_keys = ["daily_schedule", "total_study_time", "validation_passed", "notes"]
    for key in required_keys:
        if key not in output:
            output["validation_passed"] = False
            output["notes"] += f"Missing key: {key}. "

    total_time = sum(
        sum(block["duration"] for block in day["study_blocks"])
        for day in output["daily_schedule"]
    )

    output["total_study_time"] = total_time

    if total_time > 40:
        output["validation_passed"] = False
        output["notes"] += "Exceeded recommended weekly study time."

    return output
