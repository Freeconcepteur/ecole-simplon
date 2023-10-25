import streamlit as st
import requests
import time
import matplotlib.pyplot as plt

st.title('Lancé de dé')

# Dictionnaire pour stocker la fréquence de chaque résultat
frequency_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Créer un conteneur vide pour le nombre total de lancers
total_rolls_placeholder = st.empty()

# Créer des conteneurs vides pour les graphiques
bar_chart_title = st.empty()
bar_chart_placeholder = st.empty()
pie_chart_placeholder = st.empty()

total_rolls = 0  # Variable pour stocker le nombre total de lancers

while True:
    response = requests.get('http://localhost:5000/random_number')
    number = response.json()['number']
    
    # Mettre à jour le dictionnaire de fréquence avec le nouveau résultat
    frequency_dict[number] += 1
    total_rolls += 1  # Incrémenter le nombre total de lancers
    
    # Mettre à jour le nombre total de lancers
    total_rolls_placeholder.text(f"Nbr de lancés: {total_rolls}")
    
    
    
    # Mettre à jour le Bar Chart
    bar_chart_placeholder.bar_chart(frequency_dict)
    
    # Créer et mettre à jour le Pie Chart
    labels = [str(i) for i in frequency_dict.keys()]
    sizes = list(frequency_dict.values())
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    pie_chart_placeholder.pyplot(fig1)
    
    # Attendre 5 secondes avant de rafraîchir avec un nouveau résultat
    time.sleep(0.5)
