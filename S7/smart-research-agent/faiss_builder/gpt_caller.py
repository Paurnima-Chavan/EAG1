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

    def fetch_embeddings(self, sentence):
        """
        Calls OpenAI to create embeddings for the given sentences.

        Args:
            sentence (str): List of sentences for which embeddings need to be created.

        Returns:
            CreateEmbeddingResponse: Embedding response

        Raises:
            Exception: If there is an error while creating embeddings.        """

        try:

            response = self.client.embeddings.create(
                extra_headers=self.extra_headers,
                input=sentence,
                model="embeddings"
            )

            return response
        except Exception as e:
            print(f"Unable to create embeddings due to error= {str(e)}")
            raise Exception(e)

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
