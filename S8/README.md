# 🧠 Smart Research Agent – Your Browser's Memory!

Turn your browser into a searchable, intelligent research companion.  
This project indexes every webpage you visit (except private ones), embeds its content using LLMs, stores it in a FAISS index, and lets you **search your browsing history semantically** through a Chrome extension!

> TL;DR: Your browser remembers what you read. You can ask questions later — and it finds the source and highlights the answer on the original page.

---

## 🚀 Features

- ✅ Builds embeddings for each web page you visit
- ✅ Stores semantic chunks in a local **FAISS** index
- ✅ Chrome Extension lets you search using natural language
- ✅ Opens matched webpage and **highlights** the answer
- ✅ Powered by OpenAI Embeddings or local models
- ✅ Long-term memory across browsing sessions
- ✅ Bonus: Extendable for RAG + tool-use agents

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/smart-research-agent.git
cd smart-research-agent 
```

### 2. Backend (Python)
cd backend
pip install -r requirements.txt

# Then run:
python build_index.py

This script:

Loads a set of saved webpages (documents/)

Chunks them

Generates OpenAI embeddings

Builds a metadata.json file + faiss.index

Copy the generated metadata.json to chrome_extension/.

###2. Load Chrome Extension
Open Chrome → Extensions → "Manage Extensions"

Enable Developer Mode

Click "Load Unpacked"

Select the chrome_extension/ folder

Now the extension should appear in your browser toolbar!

💡 How It Works
You visit and save some webpages

You build a semantic index using build_index.py

Later, ask a question via Chrome popup

Agent searches the FAISS index

If a match is found:

Opens that page

