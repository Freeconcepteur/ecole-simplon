import streamlit as st
import pandas as pd
import back

# Titre de l'application
st.title('Gestion des utilisateurs')

# Menu pour ajouter un nouvel utilisateur
st.subheader('Ajouter un nouvel utilisateur')
nom = st.text_input('Nom')
email = st.text_input('Email')
if st.button('Ajouter'):
    back.add_user(nom, email)
    st.success(f'Utilisateur {nom} ajouté avec succès.')

# Menu pour mettre à jour un utilisateur
st.subheader('Mettre à jour un utilisateur')
user_list = back.view_users()
user_options = [f"{user[1]} ({user[2]})" for user in user_list]
user_selection = st.selectbox('Choisir un utilisateur', user_options, key='update')
if user_selection:
    user_id_to_update = user_list[user_options.index(user_selection)][0]
new_nom = st.text_input('Nouveau nom', key='update_nom')
new_email = st.text_input('Nouveau email', key='update_email')
if st.button('Mettre à jour', key='update_button') and user_id_to_update:
    back.update_user(user_id_to_update, new_nom, new_email)
    st.success(f'Utilisateur mis à jour avec succès.')

# Menu pour supprimer un utilisateur
st.subheader('Supprimer un utilisateur')
user_to_delete = st.selectbox('Choisir un utilisateur à supprimer', user_options, key='delete')
if st.button('Supprimer', key='delete_button') and user_to_delete:
    user_id_to_delete = user_list[user_options.index(user_to_delete)][0]
    back.delete_user(user_id_to_delete)
    st.success(f'Utilisateur supprimé avec succès.')

# Afficher tous les utilisateurs
st.subheader('Utilisateurs')
users = back.view_users()
if users:
    users_df = pd.DataFrame(users, columns=['ID', 'Nom', 'Email'])
    st.dataframe(users_df)
else:
    st.write('Aucun utilisateur trouvé.')
