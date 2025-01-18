from flask import jsonify, request, Blueprint
from models import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)

# LOGIN USER
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data ["email"]
    password = data["password"]

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200

    else:
        return jsonify({"error": "Either Email or Password is Incorrect"}), 404