import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    # Configuracion de base de datos SQLite
    DATABASE = os.path.join(os.getcwd(), 'prueba_python.db')    
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'p2_adress_secret_key_123')