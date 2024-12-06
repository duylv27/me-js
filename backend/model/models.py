from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Date, Column, ForeignKey
from sqlalchemy.orm import relationship, backref

database = SQLAlchemy()

class RolesUsers(database.Model):
    __tablename__ = "user_role"
    id = Column(Integer(), primary_key=True)
    user_id = Column("user_id", Integer(), ForeignKey("user.id"))
    role_id = Column("role_id", Integer(), ForeignKey("role.id"))

class User(database.Model):
    __tablename__ = 'user'
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), unique=True, nullable=False)
    password = database.Column(database.String(200), unique=True, nullable=False)
    email = database.Column(database.String(100), unique=True, nullable=False)
    roles = relationship(
        "Role", secondary="user_role", backref=backref("users", lazy="dynamic")
    )

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'roles': [role.name for role in self.roles]
        }

class Role(database.Model):
    __tablename__ = "role"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class Item(database.Model):
    __tablename__ = 'item'
    id = Column(database.Integer, primary_key=True)
    content = Column(String(1000), unique=False, nullable=False)
    priority = Column(Integer, unique=False, nullable=False)
    created_date = Column(Date, unique=False, nullable=False)
    created_by = Column(String, unique=False, nullable=False)
    updated_date = Column(Date, unique=False, nullable=False)
    status = Column(String, unique=False, nullable=True)

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