"""Flask Application"""

# load libraries
from flask import Flask, jsonify
import sys

# load modules
from src.blueprints.blueprint_x import blueprint_x
from src.blueprints.blueprint_y import blueprint_y

# init Flask app
app = Flask(__name__)

# register blueprints, ensure that all paths are versioned!(what it means?)
app.register_blueprint(blueprint_x, url_prefix="/api/v1/path_for_blueprint_x")
app.register_blueprint(blueprint_x, url_prefix="/api/v1/path_for_blueprint_y")