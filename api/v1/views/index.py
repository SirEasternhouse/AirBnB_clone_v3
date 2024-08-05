#!/usr/bin/python3
"""
Index file for API views
"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return a JSON status of the API"""
    return jsonify({"status": "OK"})
