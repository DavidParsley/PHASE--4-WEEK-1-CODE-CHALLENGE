from flask import jsonify, request, Blueprint
from models import Loan, User, db
from flask_jwt_extended import  jwt_required, get_jwt_identity


loan_bp = Blueprint("loan_bp", __name__)

# ADD A LOAN
@loan_bp.route("/loan", methods=["POST"])
def add_loan():
    data = request.get_json()

    amount = data['amount']
    interest = data['interest']
    start_date = data['start_date']
    loan_status = data['loan_status']
    user_id = data['user_id']

    chech_user_id = User.query.get(user_id)

    if not chech_user_id:
        return jsonify({"error":"User doesn't exists"}),406
    
    else:
        new_loan = Loan(amount=amount, interest=interest, start_date=start_date, loan_status=loan_status, user_id=user_id)
        
        db.session.add(new_loan)
        db.session.commit()
        return jsonify({"success":"Loan added successfully"}), 201

# FETCH ALL LOANS RELATED TO THE CURRENT USER LOGED IN
@loan_bp.route("/loans", methods=["GET"])
@jwt_required()
def fetch_loans():
    current_user_id = get_jwt_identity()
    loans = Loan.query.filter_by(user_id=current_user_id)
    loan_list = []

    for loan in loans:
        loan_list.append({
            "id": loan.id,
            "amount": loan.amount,
            "interest": loan.interest,
            "start_date": loan.start_date,
            "loan_status": loan.loan_status,
            "user_id": {"id": loan.user.id, "First Name": loan.user.first_name, "Last Name": loan.user.last_name, "Email": loan.user.email}
        })

    return jsonify(loan_list)

# FETCH A SINGLE LOAN RELATED TO THE CURRENT USER LOGED IN
@loan_bp.route("/loan/<int:loan_id>", methods=["GET"])
@jwt_required()
def fetch_loan(loan_id):
    current_user_id = get_jwt_identity()
    loan = Loan.query.filter_by(id=loan_id, user_id=current_user_id).first()

    if loan:
        loan_data = {
            "id": loan.id,
            "amount": loan.amount,
            "interest": loan.interest,
            "start_date": loan.start_date,
            "loan_status": loan.loan_status,
            "user_id": {"id": loan.user.id, "First Name": loan.user.first_name, "Last Name": loan.user.last_name, "Email": loan.user.email}
        }

        return jsonify(loan_data)
    
    return jsonify({"error": "Loan doesn't exist!"}), 406

# UPDATE A LOAN
@loan_bp.route("/loan/<int:loan_id>", methods=["PATCH"])
@jwt_required()
def update_loan(loan_id):
    current_user_id = get_jwt_identity()
    loan = Loan.query.get(loan_id)  

    if loan:
        current_user = User.query.get(current_user_id)
        if not current_user or not current_user.is_admin:
            return jsonify({"error": "Unauthorized: User is not an admin"}), 403

        data = request.get_json()
        amount = data.get('amount', loan.amount)
        interest = data.get('interest', loan.interest)
        start_date = data.get('start_date', loan.start_date)  
        loan_status = data.get('loan_status', loan.loan_status)
        user_id = data.get('user_id', loan.user_id)

        check_user_id = User.query.get(user_id)
        if not check_user_id:
            return jsonify({"error": "User doesn't exist"}), 404  
        
        loan.amount = amount
        loan.interest = interest
        loan.start_date = start_date
        loan.loan_status = loan_status
        loan.user_id = user_id

        db.session.commit()
        return jsonify({"success": "Loan updated successfully"}), 200

    return jsonify({"error": "Loan doesn't exist!"}), 404  

# DELETE A LOAN
@loan_bp.route("/loan/<int:loan_id>", methods=["DELETE"])
def delete_todos(loan_id):
    loan = Loan.query.get(loan_id)

    if loan:
        db.session.delete(loan)
        db.session.commit()
        return jsonify({"success":"Loan Deleted successfully"}), 200

    else:
        return jsonify({"error":"Loan your are trying to delete doesn't exist!"}),406


