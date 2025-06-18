from pymilvus import connections, utility
import time

print("Testing Milvus connection...")

# Try to connect with a longer timeout
try:
    connections.connect("default", host="127.0.0.1", port="19530")
    print("✓ Successfully connected to Milvus!")
    
    # Check if collection exists
    if utility.has_collection("text_embeddings"):
        print("✓ Collection 'text_embeddings' exists!")
    else:
        print("✗ Collection 'text_embeddings' does not exist!")
        
except Exception as e:
    print(f"✗ Connection failed: {e}")
    
finally:
    try:
        connections.disconnect("default")
        print("✓ Disconnected from Milvus")
    except:
        pass 