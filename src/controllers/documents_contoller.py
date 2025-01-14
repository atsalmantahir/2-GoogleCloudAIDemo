from flask import Blueprint, jsonify

# Create the Blueprint for the documents controller
documents_bp = Blueprint('documents', __name__)

# Define a simple GET endpoint
@documents_bp.route('/', methods=['GET'])
def get_documents():
    # Sample response with a list of documents (this could be dynamic in a real application)
    documents = [
        {"id": 1, "title": "Document 1", "description": "This is document 1"},
        {"id": 2, "title": "Document 2", "description": "This is document 2"}
    ]
    
    return jsonify(documents), 200
