from flask import Blueprint, request, jsonify
import logging

logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "flask-app"}), 200

@api_bp.route('/example', methods=['GET', 'POST'])
def example():
    """Example endpoint for AI upskilling exercises"""
    if request.method == 'GET':
        return jsonify({
            "message": "This is an example endpoint",
            "usage": "Add your AI/ML functionality here",
            "methods": ["GET", "POST"]
        }), 200
    
    # POST example
    data = request.get_json() or {}
    return jsonify({
        "message": "Received data",
        "data": data,
        "note": "This is where you'd process data with AI/ML models"
    }), 200

