import streamlit as st, html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# EX 1
st.title('Tableau de Bord Simple')
st.write('on va tester un bouton')

# EX 2
if st.button('Cliquez moi'):
    st.write('Vous avez cliqué sur le bouton !')

age = st.slider('Quel est votre âge', 0, 100, 25)
st.write("Vous avez ", age, 'ans')

# EX 3
nom = st.text_input('Insérez votre nom', 'Votre nom')
st.write('Bonjour', nom, ' !')

# EX 4
agree = st.checkbox('Montrer les détails')
if agree:
    st.write('Les détails sont affichés')

# EX 5

frequence = 10 
nombre_echantillons = 1000


t = np.linspace(0, 1, nombre_echantillons, endpoint=False)
signal = np.sin(2 * np.pi * frequence * t)

st.line_chart(signal)

# EX 6

st.markdown("""
        <style>
            .stButton>button {
                box-shadow: 0px 10px 14px -7px #3e7327;
                background:linear-gradient(to bottom, #77b55a 5%, #72b352 100%);background-color:#77b55a;
                border-radius:4px;border:1px solid #4b8f29;display:inline-block;
                cursor:pointer; 
                color:#ffffff; 
                font-family:Arial; 
                font-size:13px; 
                font-weight:bold;
                padding:6px 12px;
                text-decoration:none;
                text-shadow:0px 1px 0px #5b8a3c;
                border: 1px solid black
            }

            .stButton>button:hover {
                opacity: 1;
            }
        </style>
    """, unsafe_allow_html=True)

if st.button("Cliquez-moi"):
    st.write("Vous avez cliqué sur le bouton !")

# EX 7

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
   st.header("Titre 1")
   st.write('Vous êtes dans le Tab 1')

with tab2:
   st.header("Titre 2")
   st.write('Vous êtes dans le Tab 2')

with tab3:
   st.header("Titre 3")
   st.write('Vous êtes dans le Tab 3')

# EX 7

tab1, tab2 = st.tabs(["Graphique à barres", "Graphique circulaire"])
with tab1:
   st.header("Graphique à barres interactif")
   categories = ['A', 'B', 'C', 'D']
   values = [10, 30, 20, 40]
   fig, ax = plt.subplots()
   ax.bar(categories, values)
   ax.set_xlabel('Catégories')
   ax.set_ylabel('Valeurs')
   ax.set_title('Graphique à barres')
   st.pyplot(fig)

with tab2:
   st.header("Graphique circulaire interactif")
   labels = ['A', 'B', 'C', 'D']
   values = [10, 30, 20, 40]
   df = pd.DataFrame({'labels': labels, 'values': values})
   fig = px.pie(df, values='values', names='labels', title='Graphique circulaire')
   st.plotly_chart(fig)


