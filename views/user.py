from flask import jsonify, request, Blueprint
from models import User, db
from werkzeug.security import generate_password_hash

user_bp = Blueprint("user_bp", __name__)

# ADD A USER
@user_bp.route("/user", method=["POST"])
def add_user():
    data = request.get_json()
    first_name = data ["first_name"]
    last_name = data ["last_name"]
    email = data["email"]
    password = generate_password_hash(data["password"])

    check_email = User.query.filter_by(email=email).first()
    print("email", check_email)
    if check_email:
        return jsonify({"error": "Email exists"}), 404
    
    else:
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password))
        db.Session.add(new_user)
        db.Session.commit()

        return jsonify({"Success": "Added Successfully"}), 200

# UPDATE A USER INFORMATION
@user_bp.route("/user/update/<int:user_id>", method=["PATCH"])
def update_info(user_id):
    user = User.query.get(user_id)

    if user:
        data = request.get_json
        first_name = data.get(["first_name"], user.first_name)
        last_name = data.get(["last_name"], user.last_name)
        email = data.get(["email"], user.email)

        check_first_name = User.query.filter_by(first_name=first_name and id!=user.id).first()
        check_last_name = User.query.filter_by(last_name=last_name and id!=user.id).first()
        check_email = User.query.filter_by(email=email and id!=user.id).first()

        if check_first_name:
            return jsonify({"error":"First name not changed"}),406
        
        if check_last_name:
            return jsonify({"error":"Last name not changed"}),406
        
        if check_email:
            return jsonify({"error":"Email not changed"}),406
        
        else:
            user.first_name=first_name
            user.last_name=last_name
            user.email=email

            db.session.commit()
            return jsonify({"success":"Updated successfully"}), 200
        
    else:
        return jsonify({"error":"User doesn't exist!"}),406    

# UPDATE A USER PASSWORD
@user_bp.route("/user/updatepassword/<int:user_id>", method=["PATCH"])
def update_password(user_id):
    user = User.query.get(user_id)

    if user:
        data = request.get_json
        password = data.get(["password"], user.password)

        check_password = User.query.filter_by(password=password and id!=user.id).first()
        
        if check_password:
            return jsonify({"error":"Password not changed"}),406
         
        else:
            user.password=password

            db.session.commit()
            return jsonify({"success":"Updated successfully"}), 200
        
    else:
        return jsonify({"error":"User doesn't exist!"}),406            

# DELETE A USER 
user_bp.route("/user/delete_account/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"success":"Deleted successfully"}), 200

    else:
        return jsonify({"error":"User your are trying to delete doesn't exist!"}),406
