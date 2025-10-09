from src.config import *
from src.model.obra import *
from src.model.saga import *


# Create the tables in the database
with app.app_context():
    db.create_all()

print("Database created")