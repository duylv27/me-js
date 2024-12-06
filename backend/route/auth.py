from flask import jsonify, request, Blueprint

from backend.util.logger import logger
from backend.service import auth as auth_service, user as user_service

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/authenticate', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        res = {
            "message": "Authenticate successfully",
            "access_token": auth_service.login(username, password)
        }
        return jsonify(res), 200
    except ValueError as e:
        logger.error(f"Login got error: {e}")
        return jsonify({'message': 'Login Failed'}), 401

@auth_bp.route('/register', methods=['POST'])
def create():
    try:
        user = request.get_json()
        res = {
            "message": "Register successfully",
            "user": user_service.create(user).to_dict()
        }
        return jsonify(res), 200
    except Exception as e:
        logger.error(f"Register got error: {e}")
        return jsonify({'message': 'Register Failed'}), 400