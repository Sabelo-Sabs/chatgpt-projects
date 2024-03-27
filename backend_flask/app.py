from flask import Flask
from flask_cors import CORS
from routes.file_routes import file_blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains and routes

app.register_blueprint(file_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
