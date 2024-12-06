from flask import Flask
from flask_bcrypt import Bcrypt
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError, NoResultFound

from backend.model.models import User, database as db, Role
from backend.model.schemas import user_schema

from backend.util.logger import logger

app = Flask(__name__)
bcrypt = Bcrypt(app)

def create(user):
    try:
        validated_data = user_schema.load(user)
        roles_ids = validated_data.pop('roles', [])
        logger.info(f"Request body: {validated_data}")

        # check user
        exist_user = User.query.filter(
            or_(User.username == validated_data["username"], User.email == validated_data["email"])
        ).first()
        if exist_user is not None:
            logger.info("User already existed")
            raise NoResultFound("Invalid user")
        pwd = bcrypt.generate_password_hash(validated_data["password"]).decode('utf-8')
        validated_data["password"] = pwd

        # check role
        roles = Role.query.filter(Role.id.in_(roles_ids)).all()
        if len(roles) == 0:
            raise NoResultFound("Invalid Roles")

        user = User(**validated_data)
        user.roles.extend(roles)
        db.session.add(user)
        db.session.commit()

        logger.info(f"User '{user.username}' with roles {', '.join([role.name for role in roles])} created successfully.")
        return user
    except IntegrityError as e:
        db.session.rollback()
        logger.error(f"Error creating user: {e}")
        raise e
    except Exception as e:
        db.session.rollback()
        logger.error(f"Unexpected error: {e}")
        raise e