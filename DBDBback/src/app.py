from flask import Flask
from flask_cors import CORS
from src.database import db
from src.config import DATABASE_URL

# Create Flask app
app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Accept"]
    }
})

# Configure logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('flask.app')

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_EXPIRE_ON_COMMIT'] = False

# Initialize SQLAlchemy with app
db.init_app(app)

# Import models after db is set up
from src.model.obra import Obra
from src.model.saga import Saga
from src.model.raca import Raca
from src.model.transformacao import Transformacao
from src.model.personagembase import PersonagemBase
from src.model.personagemsaga import PersonagemSaga

# Import routes (after models)
from src.route.routes import *

print("Application started successfully. (reached app.py)")

# Create tables
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)