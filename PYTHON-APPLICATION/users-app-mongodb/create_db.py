from pymongo import MongoClient

# Créer une connexion au serveur MongoDB par défaut (localhost:27017)
client = MongoClient()

# Créer une référence à une base de données. 
# Si la base de données n'existe pas, elle sera créée lorsque vous insérez une première donnée.
db = client['ma_base_de_donnees']

# Créer une nouvelle collection nommée 'utilisateurs'
utilisateurs = db['utilisateurs']

# Insérer un utilisateur avec des champs 'nom' et 'email'
utilisateur = {
    'nom': 'Dupont',
    'email': 'dupont@example.com'
}

utilisateurs.insert_one(utilisateur)