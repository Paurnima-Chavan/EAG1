from models import UserInput
from perception import collect_user_input
from memory import Memory
from decision import build_schedule
from action import show_schedule
from pydantic import TypeAdapter
import os
# from dotenv import load_dotenv

# load_dotenv()

if __name__ == "__main__":
    user_raw = collect_user_input()

    # Memory step
    memory = Memory()
    memory.store(user_raw["preferences"])

    # Parse to Pydantic model
    user_data = TypeAdapter(UserInput).validate_python(user_raw)

    # LLM generates the schedule
    result = build_schedule(user_data)

    # Show the output
    show_schedule(result)
