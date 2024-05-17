import logging
import pandas as pd
import streamlit as st

#from pages.productos import extract_new_products, calculate_ids, fill_with_value, extract_bought_products

logging.basicConfig(level=logging.DEBUG)

with st.container():
    st.header("Bienvenido a Vamos Shopping!")
st.sidebar.write("Vamos Shopping!")

st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/productos.py", label="Productos")
st.page_link("pages/lista_de_la_compra.py", label="Lista de la Compra")
   