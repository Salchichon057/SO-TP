from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or '127.0.0.1' # localhost
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'root'
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'digitronikdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)