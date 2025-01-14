from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Register Blueprints (controllers)
from controllers.documents_contoller import documents_bp

app.register_blueprint(documents_bp, url_prefix='/api/documents')

# Setup Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # URL for Swagger JSON
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Document Demo API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
