from flask import jsonify, request, Blueprint
from models import Loan, User, db

loan_bp = Blueprint("loan_bp", __name__)

# ADD A LOAN
@loan_bp.route("/loan", methods=["POST"])
def add_loan():
    data = request.get_json()

    amount = data['amount']
    interest = data['interest']
    start_data = data['start_data']
    loan_status = data['loan_status']
    user_id = data['user_id']

    chech_user_id = User.query.get(user_id)

    if not chech_user_id:
        return jsonify({"error":"User doesn't exists"}),406
    
    else:
        new_loan = Loan(amount=amount, interest=interest, start_data=start_data, loan_status=loan_status, user_id=user_id)
        
        db.session.add(new_loan)
        db.session.commit()
        return jsonify({"success":"Loan added successfully"}), 201

# FETCH ALL LOANS
@loan_bp.route("/loans", methods=["GET"])
def fetch_loans():
    loans = Loan.query.all()
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

# FETCH A SINGLE LOAN
@loan_bp.route("/loan/<int:loan_id>", methods=["GET"])
def fetch_loan(loan_id):
    loan = Loan.query.get(loan_id)

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
def update_loan(loan_id):
    loan = Loan.query.get(loan_id)

    if loan:
        data = request.get_json()
        amount = data.get('amount', loan.amount)
        interest = data.get('interest', loan.interest)
        start_data = data.get('start_data', loan.start_date)
        loan_status = data.get('loan_status', loan.loan_status)
        user_id = data.get('user_id', loan.user_id)

        check_user_id = User.query.get(user_id)
        if  not check_user_id:
            return jsonify({"error": "User doesn't exist"}), 406
        
        loan.amount = amount
        loan.interest = interest
        loan.start_date = start_data
        loan.loan_status = loan_status
        loan.user_id = user_id

        db.session.commit()
        return jsonify({"success": "Updated successfully"}), 200
    
    return jsonify({"error": "Todo doesn't exist!"}), 406

# DELETE A LOAN
@loan_bp.route("/loan/<int:loan_id>", methods=["DELETE"])
def delete_todos(loan_id):
    loan = Loan.query.get(loan_id)

    if loan:
        db.session.delete(loan)
        db.session.commit()
        return jsonify({"success":"Deleted successfully"}), 200

    else:
        return jsonify({"error":"Loan your are trying to delete doesn't exist!"}),406


