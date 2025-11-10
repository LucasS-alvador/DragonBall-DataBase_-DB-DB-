import os
import sys

# Add project root to path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Also add the `src` folder to path so modules like `database` and `app` are importable
SRC = os.path.join(ROOT, 'src')
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from app import app, db
from model.obra import *
from model.saga import *
from model.raca import *
from model.transformacao import *
from model.personagembase import *
from model.personagemsaga import *

def create_db():
    # Delete existing database file if it exists
    db_path = os.path.join(ROOT, 'src', 'database.db')
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Existing database removed.")

    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    try:
        create_db()
        print("Database created successfully!")
    except Exception as e:
        print(f"Error creating database: {str(e)}")