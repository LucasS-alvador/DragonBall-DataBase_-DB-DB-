import os
import sys
from sqlalchemy import text

# Ensure project root is on sys.path so 'src' imports resolve
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.app import app, db


if __name__ == '__main__':
    with app.app_context():
        conn = db.engine.connect()
        try:
            # Check existing columns in Saga
            res = conn.execute(text("PRAGMA table_info('Saga')")).mappings().all()
            cols = [row['name'] for row in res]
            print('Saga columns:', cols)
            if 'imagem' not in cols:
                print("Adding column 'imagem' to Saga table...")
                conn.execute(text('ALTER TABLE "Saga" ADD COLUMN imagem VARCHAR(1024)'))
                print("Column 'imagem' added.")
            else:
                print("Column 'imagem' already exists; nothing to do.")
        finally:
            conn.close()
