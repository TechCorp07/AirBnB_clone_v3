#!/usr/bin/python3
""" handles all CRUD for cities """

from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State
