import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['ma_base_de_donnees']
collection = db['utilisateurs']

# Fonction pour ajouter un utilisateur
def ajouter_utilisateur(nom, email):
    utilisateur = {"nom": nom, "email": email}
    collection.insert_one(utilisateur)

# Interface de l'application Streamlit pour ajouter un utilisateur
st.title("Connexion à une Base de Données NoSQL (MongoDB)")

nom = st.text_input("Nom")
email = st.text_input("Email")

if st.button("Ajouter"):
    if nom and email:
        ajouter_utilisateur(nom, email)
        st.success(f"L'utilisateur {nom} a été ajouté avec succès !")
    else:
        st.error("Veuillez remplir tous les champs.")

# Récupération et affichage des utilisateurs après l'insertion
st.title('Liste des utilisateurs')
users = collection.find({})
for user in users:
    st.write(f"Id: {user['_id']}, Nom: {user['nom']}, Email: {user['email']}")

client.close()
