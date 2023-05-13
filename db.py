from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db = MongoClient(str(os.getenv('CONNECTION_STRING'))).teste1
jogos = db.jogos
