from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---- Search Functionality ----

def search(query, vectorizer, embeddings, sentences, top_k=3):
    # Convert query into an embedding
    query_embedding = vectorizer.transform([query])

    # Compute similarity between the query and all stored embeddings
    similarities = cosine_similarity(query_embedding, embeddings).flatten()

    # Rank results
    ranked_indices = similarities.argsort()[::-1][:top_k]

    print(f"\nSearch results for: '{query}'\n")
    for idx in ranked_indices:
        print(f"Sentence: {sentences[idx]}")
        print(f"Similarity: {similarities[idx]:.4f}\n")





# Example sentences
sentences = [
    "The cat sits on the mat.",
    "A dog lies on the carpet.",
    "I love pizza and pasta."
]

# Create TF-IDF embeddings (simple text embeddings)
vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(sentences)

# Cosine similarity is a metric used to measure how similar two vectors are,based on the angle between them rather than their magnitude
similarity_matrix = cosine_similarity(embeddings)

print("Embeddings (vector representations):\n")
print(embeddings.toarray())

print("\nSimilarity between sentences:\n")
print(similarity_matrix)



# Try some searches
search("pet on the floor", vectorizer, embeddings, sentences)
search("food", vectorizer, embeddings, sentences)
search("eatable", vectorizer, embeddings, sentences)
