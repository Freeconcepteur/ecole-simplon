import pandas as pd
import mysql.connector

# infos de connexion MySQL
serveur = 'localhost'
port = '3306'
user = 'root'
password = 'cedricl'
database ="csv_products"


big_data = pd.read_csv('produits.csv')
print(big_data)

# tableau des familles
familles = big_data['FAMILLE ARTICLE']
familles_uniques = pd.unique(familles)

#print(familles_uniques)



# tableau des conditionnements
conditionnements = big_data['CONDITION']
conditionnements_uniques = pd.unique(conditionnements)
print(conditionnements_uniques)

# Conversion des prix vers float
big_data["PU HT"] = big_data["PU HT"].str.replace(',', '.').astype(float)
print(big_data)


db = mysql.connector.connect(
    host=serveur,
    port=port,
    user=user,
    password=password
)

for i in familles_uniques :
    print (i)





