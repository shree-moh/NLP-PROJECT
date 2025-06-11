from sentence_transformers import SentenceTransformer
import numpy as np



corpus = [
    "The Colossus of Rhodes was a statue of the Greek sun-god Helios, erected in the city of Rhodes by Chares of Lindos in 280 BC.",
    "Python is a popular programming language.",
    # ... more docs
]
embedder = SentenceTransformer("all-MiniLM-L6-v2")
corpus_embeddings = embedder.encode(corpus, convert_to_numpy=True)

def retrieve(query, top_k=1):
    query_emb = embedder.encode([query], convert_to_numpy=True)[0]
    scores = np.dot(corpus_embeddings, query_emb) / (
        np.linalg.norm(corpus_embeddings, axis=1) * np.linalg.norm(query_emb) + 1e-10
    )
    top_k_idx = np.argsort(scores)[::-1][:top_k]
    return [corpus[i] for i in top_k_idx]
