from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from backend.db import dbconf
from backend.model.models import database
from backend.route.user_route import user_bp
from backend.route.item_route import item_bp

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = dbconf.SQLALCHEMY_DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.json.compact = False

migrate = Migrate(app, database)
database.init_app(app)
api = Api(app)

# read
app.register_blueprint(user_bp)
app.register_blueprint(item_bp)

with app.app_context():
    database.create_all()

if __name__ == '__main__':
    app.run(port=5555, debug=True)