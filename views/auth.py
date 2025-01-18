from flask import jsonify, request, Blueprint
from models import User

auth_bp = Blueprint("auth_bp", __name__)