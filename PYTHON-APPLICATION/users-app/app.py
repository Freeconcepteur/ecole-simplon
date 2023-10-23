import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['ma_base_de_donnees']
collection = db['utilisateurs']

st.title('Liste des utilisateurs')
users = collection.find({})
for user in users:
    st.write(f"ID: {user['user_id']}, Nom: {user['user_name']}")

