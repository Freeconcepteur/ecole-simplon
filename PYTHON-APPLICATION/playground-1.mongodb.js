/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'ma_base_de_donnees';
const collection = 'utilisateurs';

// Utiliser une nouvelle base de données.
db = db.getSiblingDB(database);

// Créer une nouvelle collection.
db.createCollection(collection);

// Insérer un document dans la collection.
db[collection].insertOne({
    user_id: 1, // Remplacez par un numéro d'utilisateur approprié
    user_name: "nom_utilisateur" // Remplacez par un nom d'utilisateur approprié
});



