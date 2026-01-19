from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "The cat sits on the mat.",
    "A dog lies on the carpet.",
    "I love pizza and pasta."
]
print(sentences)
embeddings = model.encode(sentences, convert_to_tensor=True)

query = "food"
query_embedding = model.encode(query, convert_to_tensor=True)

similarities = util.cos_sim(query_embedding, embeddings)

print(query,'->',similarities)

query = "pet on the floor"
query_embedding = model.encode(query, convert_to_tensor=True)

similarities = util.cos_sim(query_embedding, embeddings)

print(query,'->',similarities)
query = "eatable"
query_embedding = model.encode(query, convert_to_tensor=True)

similarities = util.cos_sim(query_embedding, embeddings)

print(query,'->',similarities)
