from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from config import Config
from logic.controllers.userController import UserController
from logic.dependancy import provide_user_repository
from dotenv import load_dotenv


# Créer une instance Flask
app = Flask(__name__)
load_dotenv()

# Activer CORS pour toutes les routes et toutes les origines
CORS(app)

# Injection de dépendances
user_repository = provide_user_repository()
user_controller = UserController(user_repository)

# Enregistrement des routes
user_controller.register_routes(app)

def test_mongo_connection():
    import os
    from dotenv import load_dotenv

    # Charger .env
    load_dotenv()
    db_url = os.getenv("MONGO_URI")
    if not db_url:
        print("Erreur : MONGO_URI n'est pas défini dans .env")
        return

    try:
        client = MongoClient(db_url)
        print("Connexion réussie !")
    except Exception as e:
        print("Erreur lors de la connexion :", str(e))

# Commande pour lancer le serveur en mode de développement
if __name__ == '__main__':
    test_mongo_connection()
    app.run(debug=True)

