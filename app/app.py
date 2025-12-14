"""
Flask Application for AI Up-Skilling Program

This is a starter framework designed for learning and experimenting with AI/ML features.
The structure is organized to support:
- API endpoints for AI services
- Model integration
- Utility functions
- Easy Docker deployment
"""
from flask import Flask, jsonify
from decouple import config
import logging

# Import blueprints
from routes.api import api_bp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    @app.route('/')
    def home():
        """Root endpoint with API information"""
        return jsonify({
            "message": "Welcome to AI Up-Skilling Flask App",
            "version": "1.0.0",
            "endpoints": {
                "health": "/api/health",
                "example": "/api/example"
            },
            "documentation": "See README.md for usage instructions"
        }), 200
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Endpoint not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app

app = create_app()
PORT = config('PORT', default=5000, cast=int)

if __name__ == '__main__':
    logger.info(f"Starting Flask app on port {PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)

