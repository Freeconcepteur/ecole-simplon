# main.py

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from models.models import Base, Product, Customer, Order  # Importer les modèles
from sqlalchemy.orm import sessionmaker

# Définir l'URL de la base de données
db_url = "sqlite:///tmpdb.sqlite"

# Vérifier si la base de données existe
if database_exists(db_url):
    print("La base de données existe déjà. Elle sera supprimée.")
    drop_database(db_url)  # Supprimer la base de données si elle existe
else:
    print("La base de données n'existe pas.")

# Créer une nouvelle base de données
create_database(db_url)
print("Une nouvelle base de données a été créée.")

# Créer une engine et lier à la base de données
engine = create_engine(db_url)

# Créer la table products dans la base de données
Base.metadata.create_all(engine)
print("Toutes les tables ont été créées.")

### insertion de produits 

# Créer une session
Session = sessionmaker(bind=engine)
session = Session()

# Créer des instances de la classe Product
product_1 = Product(name='Produit_1', price=100)
product_2 = Product(name='Produit_2', price=200)
product_3 = Product(name='Produit_3', price=300)

# Ajouter les instances à la session
session.add(product_1)
session.add(product_2)
session.add(product_3)

# Créer des instances de la classe Customer
customer_1 = Customer(name='user_1', email='user_1@mail.com')
customer_2 = Customer(name='user_2', email='user_2@mail.com')
customer_3 = Customer(name='user_3', email='user_3@mail.com')

# Ajouter les instances à la session
session.add(customer_1)
session.add(customer_2)
session.add(customer_3)


# Créer des instances de la classe Order
order_1 = Order(customer_id=1, product_id=1)
order_2 = Order(customer_id=1, product_id=2)
order_3 = Order(customer_id=2, product_id=1)
order_4 = Order(customer_id=2, product_id=3)
order_5 = Order(customer_id=3, product_id=2)
order_6 = Order(customer_id=3, product_id=3)

# Ajouter les instances à la session
session.add_all([order_1, order_2, order_3, order_4, order_5, order_6])

# Commit la session pour insérer les produits dans la base de données
session.commit()

# Fermer la session
session.close()

print("Les produits ont été ajoutés à la base de données.")

### Affichage des produits

# Ouvrir une nouvelle session pour exécuter une requête
session = Session()

# Exécuter une requête pour récupérer tous les produits de la table Product
products = session.query(Product).all()
customers = session.query(Customer).all()
orders = session.query(Order).all()

# Afficher les tables
print("Produits dans la base de données :")
for product in products:
    print(f"ID: {product.id}, Nom: {product.name}, Prix: {product.price}")

print("Customers dans la base de données :")
for customer in customers:
    print(f"ID: {customer.id}, Nom: {customer.name}, Mail: {customer.email}")

print("Orders dans la base de données :")
for order in orders:
    print(f"ID: {order.id}, Customer id: {order.customer_id}, product id: {order.product_id}")



### Affichage des données avec jointure multiple

# Exécuter une requête avec jointure multiple pour récupérer les données nécessaires
results = session.query(Order, Product, Customer).\
    join(Product, Order.product_id == Product.id).\
    join(Customer, Order.customer_id == Customer.id).all()

# Afficher les résultats de la jointure
print("Détails des commandes :")
for order, product, customer in results:
    print(f"Commande ID: {order.id}, Produit: {product.name}, Client: {customer.name}, Prix: {product.price}")


### Mise à jour du prix du produit

# Trouver le produit "Produit_2"
product_to_update = session.query(Product).filter_by(name='Produit_2').first()

# Vérifier si le produit a été trouvé
if product_to_update:
    # Mettre à jour le prix du produit
    product_to_update.price = 500
    # Commit la session pour sauvegarder la mise à jour
    session.commit()
    print("Le prix de 'Produit_2' a été mis à jour à 500.")
else:
    print("Le produit 'Produit_2' n'a pas été trouvé dans la base de données.")


### Suppression d'une commande

# Trouver la commande avec l'identifiant 2
order_to_delete = session.query(Order).filter_by(id=2).first()

# Vérifier si la commande a été trouvée
if order_to_delete:
    # Supprimer la commande de la session
    session.delete(order_to_delete)
    # Commit la session pour sauvegarder la suppression
    session.commit()
    print("La commande avec l'identifiant 2 a été supprimée.")
else:
    print("La commande avec l'identifiant 2 n'a pas été trouvée dans la base de données.")

# Fermer la session
session.close()


