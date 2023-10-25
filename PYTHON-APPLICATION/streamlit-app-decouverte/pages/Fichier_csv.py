import streamlit as st, html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from io import StringIO

st.title('Fichier CSV')


uploaded_file = st.file_uploader("Uploader un fichier")
if uploaded_file is not None:
    
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    
    string_data = stringio.read()
    st.write(string_data)

    
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)