from src.config import *
from src.model.car import *
from src.model.person import *

# Create the tables in the database
with app.app_context():
    db.create_all()

print("Database created")