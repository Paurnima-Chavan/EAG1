# mcp_servers/mcp_server_7_telegram_notify.py

import os
import requests
import sys
from pydantic import BaseModel
from mcp.server.fastmcp import FastMCP

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Set in your .env
mcp = FastMCP("telegram-notifier")


class TelegramNotifyInput(BaseModel):
    chat_id: int
    message: str


@mcp.tool()
def notify_user(input: TelegramNotifyInput) -> str:
    """Send a message to a Telegram user or group via bot."""
    if not TELEGRAM_TOKEN:
        return "Telegram token not set. Please add TELEGRAM_BOT_TOKEN to your .env"

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": input.chat_id,
        "text": input.message
    }

    response = requests.post(url, json=payload)
    if response.ok:
        return "✅ Message sent"
    else:
        return f"❌ Failed: {response.text}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
