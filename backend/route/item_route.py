from flask import jsonify, request, Blueprint
from sqlalchemy import Integer

from backend.logger import logger
from backend.model.models import Item
from backend.service import item as item_service

item_bp = Blueprint('items', __name__)

# read
@item_bp.route('/items', methods=['GET'])
def get():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    return jsonify(item_service.get_all(page, per_page)), 200

@item_bp.route("/items/<item_id>", methods=["GET"])
def get_by_id(item_id: Integer):
    item = Item.query.get(item_id)
    if not item:
        return {"message": "Item not found"}, 400
    return item.to_dict(), 200

# create
@item_bp.route('/items', methods=['POST'])
def post():
    try:
        data = request.get_json()
        create_item = item_service.create(data)
        response = {
            'message': 'Item added successfully',
            'item': create_item
        }
        return jsonify(response), 201
    except ValueError as e:
        logger.error(f"Create Item got error: {e}")
        return {'message': 'An error occurred while creating the item'}, 500


# update
@item_bp.route('/items/<item_id>', methods=['PUT'])
def put(item_id: Integer):
    try:
        data = request.get_json()
        updated_item = item_service.update(item_id, data)
        response = {
            "message": "Item updated successfully",
            "item": updated_item
        }
        return jsonify(response), 200
    except ValueError as e:
        logger.error(f"Update Item got error: {e}")
        return {'message': 'An error occurred while updating the item'}, 500


# delete
@item_bp.route("/items/<item_id>", methods=["DELETE"])
def delete_by_id(item_id: Integer):
    try:
        item_service.delete(item_id)
        return {'message': 'Delete Item successfully'}, 200
    except ValueError:
        return {'message': 'Delete Item failed'}, 400
