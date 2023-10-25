## Exercice 1

L'application doit afficher un titre, par exemple, "Bienvenue dans mon application Streamlit", en utilisant la fonction st.title. En dessous du titre, affichez un message d'accueil tel que "Ceci est une application Streamlit de base" en utilisant la fonction st.write.

## Widget Bouton

Ajoutez un widget bouton à votre tableau de bord en utilisant la fonction st.button. Le texte du bouton peut être "Cliquez-moi".
Lorsque l'utilisateur clique sur le bouton, affichez un message disant "Vous avez cliqué sur le bouton !" en utilisant st.write.

## Widget Curseur

Ajoutez un widget curseur pour que l'utilisateur puisse choisir son âge en utilisant la fonction st.slider. 
Le curseur doit permettre de choisir un âge entre 0 et 100, avec une valeur initiale de 25.
Affichez l'âge sélectionné en utilisant st.write, par exemple, "Vous avez {âge} ans."

## Widget Zone de Texte
Ajoutez un widget zone de texte pour que l'utilisateur puisse saisir son nom en utilisant la fonction st.text_input. 
Demandez à l'utilisateur d'entrer son nom.
Affichez un message de bienvenue personnalisé en utilisant st.write, par exemple, "Bonjour, {nom} !", où {nom} est le nom saisi par l'utilisateur.

## Widget Case à Cocher
Ajoutez un widget case à cocher en utilisant la fonction st.checkbox. 
Le texte de la case à cocher peut être "Montrez les détails".
Si l'utilisateur coche la case, affichez un message disant "Les détails sont affichés" en utilisant st.write.

## Afficher un Graphique
Utilisez NumPy pour générer un signal sinusoïdal en fonction de la fréquence sélectionnée. Vous pouvez créer un échantillon de temps t allant de 0 à 1 seconde en utilisant np.linspace et ensuite générer le signal en utilisant la formule np.sin(2 * np.pi * freq * t).
Utilisez la fonction st.line_chart pour afficher le signal sinusoïdal en fonction de la fréquence sélectionnée. Le graphique doit montrer l'évolution du signal sinusoïdal au fil du temps.

## Personnalisation des Widgets Streamlit

Utilisez du HTML pour personnaliser le bouton. Créez une chaîne de caractères button_html contenant du code HTML et CSS pour styliser le bouton. Dans l'exemple, le bouton est personnalisé avec un arrière-plan vert, une couleur de texte blanche, une bordure noire et un bord arrondi.
Utilisez la fonction st.markdown pour afficher le code HTML avec unsafe_allow_html=True pour autoriser le HTML.
Utilisez une structure conditionnelle pour afficher le message "Vous avez cliqué sur le bouton !" seulement lorsque le bouton est cliqué (c'est-à-dire, lorsque la variable button est vraie).

## Tableau de Bord avec Onglets Streamlit
Créer 3 onglets et dans chaque onglets afficher des données différentes:

Onglet "Graphique à Barres":
Si l'utilisateur sélectionne "Graphique à barres", affichez un titre ("Graphique à barres interactif").
Créez des données pour le graphique à barres, par exemple, une liste de catégories et une liste de valeurs.
Créez un graphique à barres interactif en utilisant Matplotlib.
Affichez le graphique en utilisant st.pyplot.
Onglet "Graphique Circulaire":
Si l'utilisateur sélectionne "Graphique circulaire", affichez un titre ("Graphique circulaire interactif").
Créez des données pour le graphique circulaire, par exemple, un dictionnaire avec des labels et des valeurs.
Créez un graphique circulaire interactif en utilisant Plotly Express.
Affichez le graphique en utilisant st.plotly_chart.
