import os
import sqlite3
from sqlalchemy import event
from sqlalchemy.engine import Engine
import tempfile

# Enforce FK constraints in SQLite
@event.listens_for(Engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

# Create a temporary file to be used as the test database
db_fd, test_db_path = tempfile.mkstemp()
DATABASE_URL = f"sqlite:///{test_db_path}"

print(f"Test configuration loaded successfully. Using database at: {test_db_path}")