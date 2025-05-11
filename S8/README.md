# 📚 Smart Study Plan Agent with Google Sheets and Multi-Channel Notifications

An **Agentic AI System** that receives natural language study requests from users (via terminal or Telegram), generates personalized weekly study plans using an **MCP Tool**, and delivers the result via **Google Sheets and Gmail**. It also supports **SSE-based server communication** to future-proof for web services.

---

## ✅ Features

- **Natural Language Understanding**  
  Example:  
  _"Make a weekly study plan for Science and Math for my 8th-grade exams and email it to me."_

- **Multi-Channel Interaction**  
  - CLI (Command Line)
  - Telegram Bot (User to Agent)

- **MCP Tool Execution (Stdio-based)**  
  - Runs `mcp_server_4_study_plan.py` to generate dynamic study plans.

- **Google Sheets Integration**  
  - Saves plans to Google Sheets.
  - Optionally uploads through an SSE server.

- **Gmail Notifications**  
  - Emails the sheet link to the user.

- **SSE Server Support**  
  - `/tools/upload_study_plan` endpoint for receiving and processing study plans.

---

## Google API Setup
Place your credentials.json for Google Sheets and Drive in the project root.

## Environment Variables (.env)
GMAIL_USER=your-email@gmail.com
GMAIL_PASSWORD=your-app-password
TELEGRAM_BOT_TOKEN=your-telegram-bot-token

## 🚀 How to Run
###1. Start SSE Server

uvicorn sse_server.main:app --reload --port 8000
###2. Start Telegram Listener

python telegram_listener.py
###3. Or Run Agent from CLI

python agent.py
###Provide input like:

Make a weekly study plan for Science and Math for my 8th-grade exams and email it to me.

##📨 How It Works (End-to-End)
- User sends a request via CLI or Telegram.

- Agent analyzes the request and extracts subjects, preferences, and contact info.

- Agent calls MCP Tool to generate the study plan.

- Saves to Google Sheet and emails the user.

- Optionally uploads to Google Drive using the SSE server.

## SSE Server logs
INFO:     Will watch for changes in these directories: ['C:\\PyCharm\\jbr\\bin']

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

INFO:     Started reloader process [24176] using StatReload

INFO:     Started server process [32536]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

Received upload request: title='Weekly Study Plan' rows=[['Day', 'Subject', 'Hours'], ['Friday', 'Math', '0.5'], ['Monday', 'Math', '0.5'], ['Monday', 'Science', '0.5'], ['Sunday', 'Math', '0.5'], ['Sunday', 'Science', '0.5'], ['Wednesday', 'Science', '0.5']] email='xxx@gmail.com'

https://docs.google.com/spreadsheets/d/xxxxxx

INFO:     127.0.0.1:57433 - "POST /tools/upload_study_plan HTTP/1.1" 200 OK

## telegram_listener logs
🔍 Analyzing query...

🎯 Parsed Request: Subjects=['Math', 'Science'], Grade=8th Grade, Email=paurnimach@gmail.com

🧠 Generating study plan using MCP tool...

in MultiMCP initialize
→ Scanning tools from: mcp_servers/mcp_server_4_study_plan.py in C:\TFS\other\EAG1\S8\smart-agent

Connection established, creating session...

[agent] Session created, initializing...

[agent] MCP session initialized

Processing request of type ListToolsRequest

→ Tools received: ['generate_study_plan']

→ Scanning tools from: mcp_servers/mcp_server_7_telegram_notify.py in ~\EAG1\S8\smart-agent

Connection established, creating session...

[agent] Session created, initializing...

[agent] MCP session initialized

→ Tools received: ['notify_user']

Processing request of type ListToolsRequest

Processing request of type CallToolRequest

🧠 Memory updated.

📄 Writing to Google Sheets...

Status Code: 200

✅ Google Sheet created: https://docs.google.com/spreadsheets/d/xxxxxx

📧 Sending email...

Email sent to xxxx@gmail.com

