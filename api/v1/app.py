#!/usr/bin/python3
"""
Flask application for the API
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    # Get host and port from environment variables or use defaults
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))

    # Run the Flask app
    app.run(host=host, port=port, threaded=True)
