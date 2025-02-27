from app import app
from models import db, User, Loan
from werkzeug.security import generate_password_hash
from flask import request



with app.app_context():

    # Delete all rows in the Loan and User tables
    Loan.query.delete()
    User.query.delete()

    # Create an empty list
    users = []
    loans = []

    # data = request.get_json()
    password = "goat"
    
    # Users seeds
    users.append(User(first_name = "David", last_name = "Parsley", email = "davidparsley.kakhayanga@gmail.com", password=generate_password_hash(password), is_admin = True))
    users.append(User(first_name = "Anne", last_name = "Muriuki", email = "muriukianne50@gmail.com", password=generate_password_hash(password), is_admin = False))
    users.append(User(first_name = "Hamza", last_name = "Ali", email = "hamza.ali@student.moringaschool.com", password=generate_password_hash(password), is_admin = False))
    users.append(User(first_name = "Sherlyne", last_name = "Ochieng", email = "sherlyne.ochieng@student.moringaschool.com", password=generate_password_hash(password), is_admin = False))
    users.append(User(first_name = "Abdimalik", last_name = "Omar", email = "abdimalik.omar1@student.moringaschool.com", password=generate_password_hash(password), is_admin = False))
    users.append(User(first_name = "Abdimalik", last_name = "Abdullahi", email = "abdimalik.abdullahi@student.moringaschool.com", password=generate_password_hash(password), is_admin = False))
    
    # Loans seeds
    loans.append(Loan(amount = 5000000, interest = 1.2, start_date = "01-20-2025", loan_status = "Active", user_id = 1))
    loans.append(Loan(amount = 6000000, interest = 1.5, start_date = "01-21-2025", loan_status = "Active", user_id = 2))
    loans.append(Loan(amount = 7500000, interest = 1.3, start_date = "01-22-2025", loan_status = "Paid-Off", user_id = 3))
    loans.append(Loan(amount = 4500000, interest = 1.4, start_date = "01-23-2025", loan_status = "Active", user_id = 4))
    loans.append(Loan(amount = 9000000, interest = 1.2, start_date = "01-24-2025", loan_status = "Active", user_id = 5))
    loans.append(Loan(amount = 3200000, interest = 1.6, start_date = "01-25-2025", loan_status = "Paid-Off", user_id = 6))
    loans.append(Loan(amount = 4000000, interest = 1.5, start_date = "01-26-2025", loan_status = "Active", user_id = 2))
    loans.append(Loan(amount = 8500000, interest = 1.4, start_date = "01-27-2025", loan_status = "Active", user_id = 4))
    loans.append(Loan(amount = 10000000, interest = 1.3, start_date = "01-28-2025", loan_status = "Active", user_id = 6))
    loans.append(Loan(amount = 7000000, interest = 1.6, start_date = "01-29-2025", loan_status = "Paid-Off", user_id = 5))
    loans.append(Loan(amount = 5500000, interest = 1.4, start_date = "01-30-2025", loan_status = "Active", user_id = 2))
    loans.append(Loan(amount = 6500000, interest = 1.2, start_date = "02-01-2025", loan_status = "Paid-Off", user_id = 3))
    loans.append(Loan(amount = 8000000, interest = 1.7, start_date = "02-02-2025", loan_status = "Active", user_id = 4))
    loans.append(Loan(amount = 3600000, interest = 1.5, start_date = "02-03-2025", loan_status = "Paid-Off", user_id = 5))
    loans.append(Loan(amount = 5200000, interest = 1.3, start_date = "02-04-2025", loan_status = "Active", user_id = 2))
    loans.append(Loan(amount = 9200000, interest = 1.4, start_date = "02-05-2025", loan_status = "Paid-Off", user_id = 1))
    

    # Insert each Loan and User in the list into the database tables
    db.session.add_all(users)
    db.session.add_all(loans)

    # Commit the transaction
    db.session.commit()