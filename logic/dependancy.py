import os
from dotenv import load_dotenv

from logic.repositories.mongoUserRepository import MongoUserRepository

# Charger le fichier .env
load_dotenv()

def provide_user_repository():
    db_url = os.getenv("MONGO_URI")
    db_name = "comparator_hotel"
    if not db_url:
        raise ValueError("MONGO_URI n'est pas défini dans le fichier .env")
    return MongoUserRepository(db_url, db_name)
