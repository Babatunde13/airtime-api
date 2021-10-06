import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    SECRET_KEY=os.environ.get('SECRET_KEY')
    RELOADLY_CLIENT_ID=os.environ.get('RELOADLY_CLIENT_ID')
    RELOADLY_CLIENT_SECRET=os.getenv('RELOADLY_CLIENT_SECRET')
    SQLALCHEMY_DATABASE_URI=os.getenv('DEV_DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG=True
    DEVELOPMENT = True
    ENV='development'

class ProductionConfig(Config):
    DEBUG=False

class TestingConfig(Config):
    TESTING=True
