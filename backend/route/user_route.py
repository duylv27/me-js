from flask import request, Blueprint
from backend.model.models import User, database as db

user_bp = Blueprint('users', __name__)

# read
@user_bp.route('/users', methods=['GET'])
def get():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}, 200


# create
@user_bp.route('/users', methods=['POST'])
def post():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return {'error': 'Username and email are required'}, 400
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'User added successfully'}, 201


# update
@user_bp.route('/users', methods=['PUT'])
def put(user_id):
    user = User.query.get(user_id)
    if not user:
        return {'error': 'User not found'}, 404
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return {'error': 'Username and email are required'}, 400
    user.username = username
    user.email = email
    db.session.commit()
    return {'message': 'User updated successfully'}, 200


# delete
@user_bp.route('/users', methods=['DELETE'])
def delete(user_id):
    user = User.query.get(user_id)
    if not user:
        return {'error': 'User not found'}, 404
    db.session.delete(user)
    db.session.commit()
    return {'message': 'User deleted successfully'}, 200
