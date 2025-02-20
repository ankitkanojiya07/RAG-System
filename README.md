# Retrieval Augmented Generation (RAG) System

## Overview
This project implements a Retrieval Augmented Generation (RAG) system using Weaviate as a vector database. It allows document ingestion, embedding generation, indexing, and efficient retrieval of relevant information from uploaded documents.

## Features
- Supports document ingestion in **PDF, DOCX, JSON, and TXT** formats.
- Generates embeddings using a model like OpenAI’s text-embedding or Hugging Face models.
- Stores embeddings in **Weaviate** for efficient retrieval.
- Provides a **REST API** to:
  - Upload and update documents.
  - Query documents for relevant snippets.
  - Retrieve associated metadata.
- Optimized for performance using:
  - **Document chunking** for large documents.
  - **Precomputed embeddings** to reduce query latency.
- **Deployment-ready** with cloud hosting.
- **(Bonus)** JSON data support for structured queries like min/max and aggregations.

## Architecture
1. **Document Ingestion & Embedding Generation**
   - Upload document via API.
   - Convert document text to embeddings.
   - Store embeddings in Weaviate.
2. **Query Processing**
   - Accept user queries via API.
   - Retrieve relevant document snippets from Weaviate.
   - Return the best-matching result with metadata.
3. **Performance Optimizations**
   - Document chunking for better retrieval.
   - Precomputed embeddings for low-latency responses.

## API Endpoints
### 1. Document Ingestion
#### Upload Document
```
POST /api/upload
```
**Request:**
```json
{
  "file": "<uploaded_file>",
  "filename": "document.pdf"
}
```
**Response:**
```json
{
  "document_id": "12345",
  "message": "Document uploaded successfully"
}
```

#### Update Document (Re-upload)
```
POST /api/update
```
Same request structure as `/api/upload`.

### 2. Query Endpoint
```
GET /api/query?document_id=12345&query=What is AI?
```
**Response:**
```json
{
  "snippet": "AI stands for Artificial Intelligence...",
  "document_id": "12345"
}
```

### 3. JSON Data Queries (Bonus)
```
GET /api/json-query?document_id=67890&operation=max&field=price
```
**Response:**
```json
{
  "max_value": 5000
}
```

## Deployment
The application is deployed on **[Your Cloud Provider]** and accessible at:
```
https://your-deployed-url.com
```

### Local Setup
#### Prerequisites
- Python 3.9+
- Weaviate running locally or on a cloud instance
- Required Python packages in `requirements.txt`

#### Installation
```
git clone https://github.com/yourrepo/rag-system.git
cd rag-system
pip install -r requirements.txt
```

#### Running the Server
```
python app.py
```

## Future Enhancements
- Implement fine-tuning for better query responses.
- Enhance JSON query capabilities.
- Improve indexing strategy for more efficient retrieval.

## Author
[Your Name]

---
Thank you for reviewing this project. Feel free to reach out for any clarifications!
