from src.config import *
from src.model.obra import *
from src.model.saga import *
from src.model.raca import *
from src.model.transformacao import *
from src.model.personagembase import *
from src.model.personagemsaga import *


# Create the tables in the database
with app.app_context():
    db.create_all()

print("Database created")