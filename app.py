from flask import Flask
from flask_migrate import Migrate
from models import  db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
migrate = Migrate(app, db)
db.init_app(app)

from views import *

app.register_blueprint(user_bp)