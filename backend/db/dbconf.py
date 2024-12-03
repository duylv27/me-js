from os import getenv, path

from dotenv import load_dotenv

# Load variables from .env
basedir = path.abspath(path.join(path.dirname(__file__), '..', 'conf'))
load_dotenv(path.join(basedir, ".env"))

# Database connection variables
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")
DB_CERT_FILE = getenv("DB_CERT_FILE")

SQLALCHEMY_DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Reset data after each run
CLEANUP_DATA = False