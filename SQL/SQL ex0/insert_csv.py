import mysql.connector
import pandas as pd

# Paramètres de connexion à la base de données
db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "cedricl",
    "database": "csv_prdts"
}

# Adresse du fichier CSV à modifier
CSV_PATH = "produits.csv"

# Fonction pour établir une connexion et la retourner
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Fonction pour insérer des données dans la base de données
def insert_data_to_db(csv_filename):
    # Lire le fichier CSV
    df = pd.read_csv(csv_filename)
    
    # Convertir la colonne 'PU HT' en format décimal
    df["PU HT"] = df["PU HT"].str.replace(',', '.').astype(float)

    # Connecter à la base de données
    connection = get_db_connection()
    cursor = connection.cursor()

    # Insérer les valeurs uniques dans 'famille' et 'conditionnement' et obtenir leurs IDs
    for index, row in df.iterrows():
        # Pour famille
        cursor.execute("SELECT id FROM `famille` WHERE `name`=%s", (row["FAMILLE ARTICLE"],))
        result = cursor.fetchone()
        if result:
            famille_id = result[0]
        else:
            cursor.execute("INSERT INTO `famille` (`name`) VALUES (%s)", (row["FAMILLE ARTICLE"],))
            famille_id = cursor.lastrowid

        # Pour conditionnement
        cursor.execute("SELECT id FROM `conditionnement` WHERE `name`=%s", (row["CONDITION"],))
        result = cursor.fetchone()
        if result:
            conditionnement_id = result[0]
        else:
            cursor.execute("INSERT INTO `conditionnement` (`name`) VALUES (%s)", (row["CONDITION"],))
            conditionnement_id = cursor.lastrowid

        # Insérer dans 'produits'
        cursor.execute(
            "INSERT INTO `produits` (`libelle`, `prix`, `code_art`, `famille_id`, `conditionnement_id`) VALUES (%s, %s, %s, %s, %s)",
            (row["LIBELLE ARTICLE"], row["PU HT"], row["Code article"], famille_id, conditionnement_id)
        )

    # Valider les changements et fermer la connexion
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    # Insérer les données du CSV dans la base de données
    insert_data_to_db(CSV_PATH)
