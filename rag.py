from flask import Flask, request, jsonify
import weaviate
from weaviate.classes.init import Auth
import weaviate.classes as wvc
from datetime import datetime

app = Flask(__name__)

def get_weaviate_client():
    return weaviate.connect_to_weaviate_cloud(
        cluster_url="https://i7vupjw7rsaethdouqfvtw.c0.australia-southeast1.gcp.weaviate.cloud",
        auth_credentials=Auth.api_key("mvFH0PPRZ7kdN6M4oi6BPIaBNkbGuJVDCRxV"),
        headers={
            "X-OpenAi-Api-Key": chatgpt
        }
    )

@app.route('/api/customers/search', methods=['GET'])
def search_customers():
    try:
        client = get_weaviate_client()
        query = request.args.get('query', '')
        limit = int(request.args.get('limit', 10))

        result = (
            client.collections.get("Customers")
            .query.near_text(
                query=query,
                limit=limit
            )
            .do()
        )

        return jsonify({"status": "success", "results": result.objects})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/customers/filter', methods=['GET'])
def filter_customers():
 
    try:
        client = get_weaviate_client()
        customers = client.collections.get("Customers")
        
        filters = []
        
        # Build filters based on provided parameters
        if request.args.get('membership'):
            filters.append(
                wvc.query.Filter.by_property("membership").equal(request.args.get('membership'))
            )
            
        if request.args.get('min_age'):
            filters.append(
                wvc.query.Filter.by_property("age").greater_than(int(request.args.get('min_age')))
            )
            
        if request.args.get('max_age'):
            filters.append(
                wvc.query.Filter.by_property("age").less_than(int(request.args.get('max_age')))
            )
            
        if request.args.get('min_spent'):
            filters.append(
                wvc.query.Filter.by_property("total_spent").greater_than(float(request.args.get('min_spent')))
            )
            
        if request.args.get('category'):
            filters.append(
                wvc.query.Filter.by_property("preferred_category").equal(request.args.get('category'))
            )

        limit = int(request.args.get('limit', 10))

        query = customers.query.get(
            limit=limit,
            filters=filters
        )
        
        result = query.do()
        
        return jsonify({"status": "success", "results": result.objects})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/customers/analyze', methods=['GET'])
def analyze_customers():
    try:
        client = get_weaviate_client()
        question = request.args.get('question', '')
        
        if not question:
            return jsonify({"status": "error", "message": "Question parameter is required"}), 400

        result = (
            client.collections.get("Customers")
            .generate.near_text(
                query=question,
                limit=1
            )
            .do()
        )

        return jsonify({"status": "success", "answer": result.generated})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
  
    try:
        client = get_weaviate_client()
        
        result = (
            client.collections.get("Customers")
            .query.get(
                filters=[wvc.query.Filter.by_property("customer_id").equal(customer_id)]
            )
            .do()
        )
        
        if not result.objects:
            return jsonify({"status": "error", "message": "Customer not found"}), 404
            
        return jsonify({"status": "success", "customer": result.objects[0]})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
