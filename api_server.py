import os

# Clear proxy environment variables to avoid local connection issues
# reference: https://stackoverflow.com/questions/79286621/unable-to-connect-to-milvus-database-using-pymilvus-with-standalone-deployment-v
os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""

from flask import Flask, request, jsonify
from pymilvus import connections, Collection
from sentence_transformers import SentenceTransformer
print("Flask server starting...")
# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# Load collection
collection = Collection("text_embeddings")
collection.load()

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Set up Flask app
app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    query_text = request.json.get('query', '')
    query_embedding = model.encode([query_text])

    results = collection.search(
        data=query_embedding,
        anns_field="embedding",
        param={"metric_type": "COSINE", "params": {"ef":128}},
        limit=5
    )

    matches = [{"text": result.entity.get("text"), "score": result.distance} for result in results[0]]

    return jsonify(matches)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
# To run the server, use the command: python api_server.py