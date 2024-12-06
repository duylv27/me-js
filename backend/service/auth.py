from flask import jsonify, Flask
from flask_bcrypt import Bcrypt

from backend.util import logger
from backend.util.logger import logger
from backend.model.models import User
from backend.util.security import create_jwt

app = Flask(__name__)
bcrypt = Bcrypt(app)

def login(username, password):
    logger.info(f'Received data: {username}')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return create_jwt(user)
    else:
        return jsonify({'message': 'Login Failed'}), 401