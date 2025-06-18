# Reference link: https://jimmy-wang-gen-ai.medium.com/milvus-a-complete-example-of-how-to-use-vectordb-by-python-and-serve-it-as-an-api-3a05e2f8db3c

from pymilvus import connections, utility
from pymilvus import CollectionSchema, FieldSchema, DataType, Collection
from pymilvus import Index # When indexing the embedding field
from sentence_transformers import SentenceTransformer
# Connect to Milvus server - local or cloud
connections.connect("default", host="localhost", port="19530")

#Check connection
if utility.has_collection("text_embeddings"):
    print("Connected to Milvus and collection exists.")
else:
    print("Milvus not connected.")

# Creating the collection:

#Defining the Collection Schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=512)
]

# Creating a collection schema
schema = CollectionSchema( fields, description= "Text and Embeddings Collection")

# Creating the collection
collection = Collection(name="text_embeddings", schema=schema)

# Indexing the embedding field to improve search performance
index_params = {"index_type": "HNSW", "params": {"M":16, "efConstruction": 200}, "metric_type": "COSINE"}
index = Index(collection, "embedding", index_params)

model = SentenceTransformer('all-MiniLM-L6-v2')


# Sample texts:
texts = [
    "Milvus is an open-source vector database.",
    "Milvus helps you store and search vector embeddings.",
    "You can use Milvus for similarity search."
]

# Generating embeddings for the sample texts
embeddings = model.encode(texts)

# Insert the data (texts, embeddings) into the collection
data = [embeddings, texts]
collection.insert(data)


# Load the collection (helps optimise query performance)
collection.load()

# Example text query
query_text= "What is Milvus"

# Generate embedding for the query text
query_embedding = model.encode([query_text])

# Perform a vector search for similar texts
results = collection.search(
    data = query_embedding,
    anns_field = "embedding",
    param = {"metric_type": "COSINE", "params": {"ef":128}},
    limit = 2, # Number of results to return
    expr = None # Optional filtering expression
)

# Print the results
for result in results[0]:
    print(f"Matched text: {result.entity.get('text')}, similarity score: {result.distance}")

# Example update: Replace a specific text based on ID
new_text = "Milvus is a vector database optimized for embeddings."

# Assuming we want to update the text with ID 1:
collection.update(expr="id == 1", data={"text": new_text})

# Delete an entry with ID 1
collection.delete(expr="id == 1")