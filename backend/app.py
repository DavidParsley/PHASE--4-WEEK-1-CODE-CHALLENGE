from flask import Flask
from flask_migrate import Migrate
from models import  db, TokenBlocklist
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_mail import Mail, Message



app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'david.kakhayanga@student.moringaschool.com'
app.config['MAIL_PASSWORD'] = 'fmtq qpff mgyl gbnn'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
migrate = Migrate(app, db)
db.init_app(app)

app.config["JWT_SECRET_KEY"] = "dgjhjhgjllijikmuh"  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=45)

jwt = JWTManager(app)
jwt.init_app(app)


from views import *

app.register_blueprint(user_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(auth_bp)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None