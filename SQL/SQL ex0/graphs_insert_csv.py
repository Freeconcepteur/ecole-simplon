# Connecting to mysql database
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
 
 
mydb = mysql.connector.connect(host="localhost",
                               port="3306",
                               user="root",
                               password="cedricl",
                               database="csv_prdts")
mycursor = mydb.cursor()

# SELECT famille_id, COUNT(*) AS `nbr` FROM csv_prdts.produits GROUP BY famille_id

# Fetching Data From mysql to my python program
mycursor.execute("SELECT a.famille_id, b.name, COUNT(*) AS `nbr` FROM csv_prdts.produits AS a INNER JOIN csv_prdts.famille AS b ON a.famille_id = b.id GROUP BY a.famille_id")
result = mycursor.fetchall


print(result)