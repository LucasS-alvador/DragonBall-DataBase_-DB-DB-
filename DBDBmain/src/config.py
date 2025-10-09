from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_cors import CORS

from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

from datetime import date

from typing import List, Optional

import os

from sqlalchemy import event
from sqlalchemy.engine import Engine
import sqlite3

# Enforce FK constraints in SQLite
@event.listens_for(Engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):  # Only for SQLite
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


class Base(DeclarativeBase):
  pass

DATABASE_URL = ""

# persistency of classes were tested in 
# sqlite and mysql, in 17/07/2025
# default configuration: sqlite
MY_DB = "SQLITE"

# Accessing an environment variable directly
try:
    db_env = os.environ['MY_DB']
    if db_env == "SQLITE":
      pass # already defined
    if db_env == "MYSQL":
      MY_DB = "MYSQL"
except KeyError:
    print("MY_DB environment variable is not set, considering default database: SQLITE.")

if MY_DB == "SQLITE":
    # some commands to make the database be created
    # at this folder
#import os
    this_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(this_path, 'database.db')
    DATABASE_URL = f"sqlite:///{file_path}"

elif MY_DB == "MYSQL":
    # mysql connection
    DATABASE_URL = "mysql+pymysql://sira:minhasenha@localhost/database"

# create the app
app = Flask(__name__)
CORS(app)

# Configure the SQLAlchemy URI (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary modification tracking

# initialize the app with the extension
db = SQLAlchemy(app)

print("Configuration loaded successfully. (reached config.py)")
