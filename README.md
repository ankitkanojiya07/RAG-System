# Customer Search API

This is a Flask-based API that integrates with Weaviate for customer data retrieval, filtering, and analysis. It provides endpoints to search, filter, analyze, and retrieve customer data.

## Features
- **Search Customers**: Retrieve customers based on a query.
- **Filter Customers**: Filter customers based on membership, age, total spent, and preferred category.
- **Analyze Customers**: Use a question-answering system to generate insights from customer data.
- **Retrieve Customer Details**: Fetch details of a specific customer by their ID.

## Setup Instructions
### Prerequisites
- Python 3.7+
- `pip` package manager
- Weaviate account and API key

### Installation
1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install the dependencies:
   ```sh
   pip install flask weaviate-client
   ```

## Environment Variables
Update the `get_weaviate_client()` function with your Weaviate API key and cluster URL.

## API Endpoints
### 1. Search Customers
**Endpoint:** `GET /api/customers/search`
**Query Parameters:**
- `query`: Search query
- `limit`: Number of results to return (default: 10)

**Example Request:**
```sh
curl "http://127.0.0.1:5000/api/customers/search?query=John&limit=5"
```

### 2. Filter Customers
**Endpoint:** `GET /api/customers/filter`
**Query Parameters:**
- `membership`: Membership type
- `min_age`: Minimum age
- `max_age`: Maximum age
- `min_spent`: Minimum total spent
- `category`: Preferred category
- `limit`: Number of results to return (default: 10)

**Example Request:**
```sh
curl "http://127.0.0.1:5000/api/customers/filter?min_age=25&max_age=40&limit=5"
```

### 3. Analyze Customers
**Endpoint:** `GET /api/customers/analyze`
**Query Parameters:**
- `question`: The question to analyze customer data

**Example Request:**
```sh
curl "http://127.0.0.1:5000/api/customers/analyze?question=What is the most common membership type?"
```

### 4. Get Customer by ID
**Endpoint:** `GET /api/customers/<customer_id>`
**Path Parameter:**
- `customer_id`: The ID of the customer

**Example Request:**
```sh
curl "http://127.0.0.1:5000/api/customers/123"
```

## Running the Application
To start the Flask server, run:
```sh
python rag.py
```

The server will be available at `http://127.0.0.1:5000`.

## Deployment
You can deploy this application to a cloud platform like AWS, GCP, Azure, Render, or Railway.

## License
This project is licensed under the MIT License.
