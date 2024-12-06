from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity

from backend.model.models import User
from datetime import timedelta

from flask_jwt_extended import create_access_token, get_jwt_identity

from backend.model.models import User


def create_jwt(user: User):
    claims = {
        'id': str(user.id),
        'username': user.username,
        'email': user.email
    }
    return create_access_token(
        identity=str(claims),
        expires_delta=timedelta(hours=1)
    )

def get_current_user() -> User | None:
    user = get_jwt_identity()
    if user is None:
        return None
    return user