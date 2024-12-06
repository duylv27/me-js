from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from backend.db import dbconf
from backend.model.models import database
from backend.route.auth import auth_bp
from backend.route.user import user_bp
from backend.route.item import item_bp

app = Flask(__name__)
CORS(app)

# SQLAlchemy Config
app.config['SQLALCHEMY_DATABASE_URI'] = dbconf.SQLALCHEMY_DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Security Config
app.config['SECRET_KEY'] = 'your_strong_secret_key'
app.config["JWT_SECRET_KEY"] = 'your_jwt_secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['headers']

app.json.compact = False

migrate = Migrate(app, database)
database.init_app(app)
api = Api(app)
jwt = JWTManager(app)

# route registry
app.register_blueprint(user_bp)
app.register_blueprint(item_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    database.create_all()

if __name__ == '__main__':
    app.run(port=5555, debug=True)