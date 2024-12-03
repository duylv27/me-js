
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Date

database = SQLAlchemy()

class User(database.Model):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), unique=True, nullable=False)
    email = database.Column(database.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Item(database.Model):
    __tablename__ = 'item'
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(String(1000), unique=False, nullable=False)
    priority = database.Column(Integer, unique=False, nullable=False)
    created_date = database.Column(Date, unique=False, nullable=False)
    created_by = database.Column(String, unique=False, nullable=False)
    updated_date = database.Column(Date, unique=False, nullable=False)
    status = database.Column(String, unique=False, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'priority': self.priority,
            'created_date': self.created_date,
            'created_by': self.created_by,
            'updated_date': self.updated_date,
            'status': self.status
        }