import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('DB_HOST')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
NAME = os.getenv('DB_NAME')



SECRET_KEY = os.getenv('SECRET_KEY')
