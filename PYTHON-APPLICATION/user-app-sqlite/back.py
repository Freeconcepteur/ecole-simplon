import sqlite3

def connect_db():
    return sqlite3.connect('ma_base_de_donnees2.db')

def create_table():
    connexion = connect_db()
    curseur = connexion.cursor()
    curseur.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')
    connexion.commit()
    connexion.close()

def add_user(nom, email):
    connexion = connect_db()
    curseur = connexion.cursor()
    curseur.execute('INSERT INTO utilisateurs (nom, email) VALUES (?, ?)', (nom, email))
    connexion.commit()
    connexion.close()

def view_users():
    connexion = connect_db()
    curseur = connexion.cursor()
    curseur.execute('SELECT * FROM utilisateurs')
    users = curseur.fetchall()
    connexion.close()
    return users

def update_user(user_id, nom, email):
    connexion = connect_db()
    curseur = connexion.cursor()
    curseur.execute('UPDATE utilisateurs SET nom = ?, email = ? WHERE id = ?', (nom, email, user_id))
    connexion.commit()
    connexion.close()

def delete_user(user_id):
    connexion = connect_db()
    curseur = connexion.cursor()
    curseur.execute('DELETE FROM utilisateurs WHERE id = ?', (user_id,))
    connexion.commit()
    connexion.close()

# Vous pouvez décommenter les lignes ci-dessous pour tester les fonctions
#create_table()
#add_user('John Doe', 'john@example.com')
#print(view_users())
