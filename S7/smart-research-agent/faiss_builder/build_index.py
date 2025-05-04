import json
import os
from urllib.parse import urlparse

import faiss
import numpy as np
import requests
from bs4 import BeautifulSoup
from gpt_caller import GPTCaller


# Configuration
CHUNK_SIZE = 200  # number of words
CHUNK_OVERLAP = 30
OUTPUT_FAISS_FILE = "index.faiss"
OUTPUT_META_FILE = "metadata.json"

urls = [
    "https://en.wikipedia.org/wiki/Natural_language_processing",
    "https://medium.com/@seanfalconer/the-future-of-ai-agents-is-event-driven-9e25124060d6",
    "https://medium.com/@mikeykusuma/the-perfect-moment-doesnt-exist-dd3787305a22"
]


def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []
    for i in range(0, len(words), size - overlap):
        chunk = " ".join(words[i:i + size])
        chunks.append(chunk)
    return chunks


def get_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for s in soup(["script", "style", "header", "footer", "nav"]):
            s.decompose()
        return soup.get_text(separator=" ", strip=True)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""


if __name__ == "__main__":
    all_embeddings = []
    metadata = []

    for url in urls:
        print(f"\nProcessing: {url}")
        text = get_text_from_url(url)
        chunks = chunk_text(text)
        gpt_client = GPTCaller()

        for idx, chunk in enumerate(chunks):
            short_chunk = " ".join(chunk.split()[:30])  # take first 30 words only
            try:
                embedding = gpt_client.fetch_embeddings(chunk)
                all_embeddings.append(np.array(embedding.data[0].embedding, dtype=np.float32))
                metadata.append({
                    "url": url,
                    "chunk_id": f"{urlparse(url).netloc}_{idx}",
                    "text": short_chunk
                })
            except Exception as e:
                print(f"Failed embedding chunk {idx}: {e}")

    # Build FAISS index
    if all_embeddings:
        dimension = len(all_embeddings[0])
        index = faiss.IndexFlatL2(dimension)
        index.add(np.stack(all_embeddings))
        faiss.write_index(index, OUTPUT_FAISS_FILE)

        with open(OUTPUT_META_FILE, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        print(f"\nIndexed {len(all_embeddings)} chunks.")
        print(f"Saved FAISS index to {OUTPUT_FAISS_FILE}")
        print(f"Saved metadata to {OUTPUT_META_FILE}")
    else:
        print("No embeddings generated.")
