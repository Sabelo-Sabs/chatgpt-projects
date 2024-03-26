from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes.file_routes import file_blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains and routes

app.register_blueprint(file_blueprint)

# Swagger UI configuration
SWAGGER_URL = '/docs'  # URL for accessing Swagger UI
API_DOCS_URL = '/static/docs'  # URL for exposing the YAML documentation files

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_DOCS_URL,
    config={'app_name': "Flask File Operations API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
