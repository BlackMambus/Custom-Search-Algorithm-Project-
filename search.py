documents = [
    "Python is a great programming language for data science.",
    "Machine learning and deep learning are subsets of AI.",
    "Python can be used for web development with frameworks like Django and Flask.",
    "Data analysis and visualization are key skills in data science.",
    "Artificial intelligence is transforming many industries."
]
import re
from collections import Counter

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def compute_score(query_tokens, doc_tokens):
    doc_counter = Counter(doc_tokens)
    return sum(doc_counter[token] for token in query_tokens)

def search(query, documents):
    query_tokens = tokenize(query)
    results = []

    for idx, doc in enumerate(documents):
        doc_tokens = tokenize(doc)
        score = compute_score(query_tokens, doc_tokens)
        if score > 0:
            results.append((idx, score, doc))

    # Sort by score descending
    results.sort(key=lambda x: x[1], reverse=True)
    return results
query = "python data science"
results = search(query, documents)

print(f"\n🔍 Results for query: '{query}'\n")
for idx, score, doc in results:
    print(f"[Score: {score}] {doc}")



