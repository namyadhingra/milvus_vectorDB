# Milvus VectorDB Example Repository

This repository provides a practical example of using [Milvus](https://milvus.io/), an open-source vector database, to manage text embeddings and perform similarity search operations via Python scripts and a simple API.

---

## Features

- **Connect to Milvus**: Establish a connection to a running Milvus server.
- **Create Collection**: Define and create a collection for storing text embeddings.
- **Insert Data**: Add texts and their embeddings to the collection.
- **Query**: Search for texts similar to a given query using vector similarity.
- **Update**: Modify existing entries in the collection.
- **Delete**: Remove entries from the collection.
- **API**: Expose a REST API for querying Milvus using Flask[#].

---

## Getting Started

### Prerequisites

- **Docker** (for running Milvus server)
- **Python 3.7+**
- **Dependencies**: Install required Python packages:
  ```
  pip install pymilvus sentence-transformers flask
  ```

### Running Milvus

1. **Start Docker**: Ensure Docker is running on your system.
2. **Start Milvus Containers**: Use the provided `docker-compose.yml` to spin up Milvus:
   ```bash
   docker-compose up -d
   ```
3. **Check Containers**: Verify that Milvus containers are up and running.

### Port Information

- **Port 19530**: This is the default gRPC port used by Milvus for SDK connections. Ensure this port is open.
---

When connecting to Milvus, you may encounter the following error:

```
pymilvus.exceptions.MilvusException: <MilvusException: (code=2, message=Fail connecting to server on localhost:19530, illegal connection params or server unavailable)>
```

---
## Script Workflow: `milvus_manage_text_embeddings.py`

This script demonstrates the following steps[#]:

1. **Connect to Milvus**
2. **Create a Collection for Text Embeddings**
3. **Insert Text and Embeddings**
4. **Query for Similar Texts**
5. **Update an Existing Entry**
6. **Delete an Entry**
7. **API to Query from Milvus**

For a detailed walkthrough and code reference, see [this tutorial](https://jimmy-wang-gen-ai.medium.com/milvus-a-complete-example-of-how-to-use-vectordb-by-python-and-serve-it-as-an-api-3a05e2f8db3c).

---

About the `without_api` Folder
This folder contains scripts that focus on direct interaction with Milvus for tasks such as connecting, inserting, querying, updating, and deleting embeddings, similar to the main workflow but without the Flask API interface.

Note:
The scripts in the without_api folder are currently not working. Troubleshooting and updates are required.

---

## References

- [Milvus Documentation](https://milvus.io/docs/overview.md)
- [Milvus Example Tutorial](https://jimmy-wang-gen-ai.medium.com/milvus-a-complete-example-of-how-to-use-vectordb-by-python-and-serve-it-as-an-api-3a05e2f8db3c)
