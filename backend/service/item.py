from typing import List, Optional, Any, Dict

from sqlalchemy import Integer
from sqlalchemy.exc import NoResultFound

from backend.util.logger import logger
from backend.model.models import Item
from backend.model.models import database as db
from backend.model.schemas import item_schema

def get_all(page: Optional[int] = 0, per_page: Optional[int] = 10) -> List[Item]:
    items = Item.query.paginate(page=page, per_page=per_page)
    items_data = [item.to_dict() for item in items]
    return items_data

def create(item_data: Any) -> Dict[str, Any]:
    try:
        logger.info(f"Request {item_data}")
        validated_data = item_schema.load(item_data)
        item = Item(**validated_data)
        db.session.add(item)
        db.session.commit()
        db.session.refresh(item)
        return item.to_dict()
    except Exception as e:
        db.session.rollback()
        logger.error(f"Database error: {e}")
        raise e

def update(item_id: Integer, item_data: Any) -> Dict[str, Any]:
    try:
        item = get_by_id(item_id)
        logger.info(f"Request {item_data}")
        validated_data = item_schema.load(item_data)
        for key, value in validated_data.items():
            setattr(item, key, value)
        db.session.commit()
        return item.to_dict()
    except Exception as e:
        db.session.rollback()
        logger.error(f"Database error: {e}")
        raise e

def delete(item_id: Integer):
    try:
        item = get_by_id(item_id)
        db.session.delete(item)
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise e

def get_by_id(item_id):
    item = Item.query.get(item_id)
    if not item:
        raise NoResultFound("Item not found")
    return item


