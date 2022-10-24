#!/usr/bin/python3
"""handles all CRUD RestFul API actions for states"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
