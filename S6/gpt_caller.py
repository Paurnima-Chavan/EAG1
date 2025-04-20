import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

class GPTCaller:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            api_version=os.getenv("OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("OPENAI_API_BASE")
        )

        self.model = os.getenv("OPENAI_API_MODEL")
       

    def query_gpt(self, chat_history, tools=None):
        try:
            kwargs = {
                "extra_headers": self.extra_headers,
                "model": self.model,
                "messages": chat_history
            }
            if tools:
                kwargs["tools"] = tools

            response = self.client.chat.completions.create(**kwargs)
            return response
        except Exception as e:
            print(f"GPT query failed: {e}")
            return None


# 🧪 Quick test
if __name__ == "__main__":
    gpt = GPTCaller()
    chat_history = [{"role": "user", "content": "Who is the PM of India?"}]
    res = gpt.query_gpt(chat_history)
    if res:
        print("Response:", res.choices[0].message.content)
