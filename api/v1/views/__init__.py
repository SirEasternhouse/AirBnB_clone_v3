#!/usr/bin/python3
"""
Initialize the views package
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from api.v1.views.amenities import *
import os

from flask import Blueprint

# Create the app_views Blueprint with the url prefix /api/v1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
