from flask import jsonify, request, Blueprint
from backend.model.models import Item, database as db
from backend.model.schemas import item_schema

from backend.logger import logger

item_bp = Blueprint('items', __name__)

# read
@item_bp.route('/items', methods=['GET'])
def get():
    items = Item.query.all()
    # Convert the list of items to a list of dictionaries
    items_data = [item.to_dict() for item in items]

    # Return the data as JSON
    return jsonify(items_data), 200

# create
@item_bp.route('/items', methods=['POST'])
def post():
    data = request.get_json()
    logger.info(f"Request {data}")
    validated_data = item_schema.load(data)
    item = Item(**validated_data)
    db.session.add(item)
    db.session.commit()
    return {'message': 'Item added successfully'}, 201


# update
# @item_bp.route('/items', methods=['PUT'])
# def put(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return {'error': 'User not found'}, 404
#     data = request.get_json()
#     username = data.get('username')
#     email = data.get('email')
#     if not username or not email:
#         return {'error': 'Username and email are required'}, 400
#     user.username = username
#     user.email = email
#     db.session.commit()
#     return {'message': 'User updated successfully'}, 200
#
#
# # delete
# @item_bp.route('/items', methods=['DELETE'])
# def delete(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return {'error': 'User not found'}, 404
#     db.session.delete(user)
#     db.session.commit()
#     return {'message': 'User deleted successfully'}, 200
