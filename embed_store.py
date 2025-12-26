
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def build_faiss(papers):
    texts = [p["abstract"] for p in papers]
    embeddings = model.encode(texts, show_progress_bar=True)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, texts
