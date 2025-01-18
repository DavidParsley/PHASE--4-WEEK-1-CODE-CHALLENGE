from flask import Flask
from flask_migrate import Migrate
from models import  db
from flask_jwt_extended import JWTManager
from datetime import timedelta


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
migrate = Migrate(app, db)
db.init_app(app)

app.config["JWT_SECRET_KEY"] = "dgjhjhgjllijikmuh"  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

jwt = JWTManager(app)
jwt.init_app(app)


from views import *

app.register_blueprint(user_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(auth_bp)