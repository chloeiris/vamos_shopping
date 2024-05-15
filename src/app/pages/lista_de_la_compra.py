import pandas as pd
import streamlit as st
import logging

logging.basicConfig(level=logging.DEBUG)
path_productos_en_t = "src/app/data/productos_en_tiendas.csv"
path_productos = "src/app/data/productos.csv"
path_productos_comprar = "src/app/data/comprar_productos.csv"

st.header("Lista de la Compra")

productos_comprar = pd.read_csv(path_productos_comprar, index_col=0, encoding='utf-8')
if productos_comprar.duplicated().sum() == 0:
    productos_en_tiendas = pd.read_csv(path_productos_en_t, index_col=0, encoding='utf-8')
    lista_compra = productos_comprar.merge(productos_en_tiendas, on="id_producto", how="left")
    logging.info("Lista de la compra calculada!")

    st.data_editor(lista_compra)
logging.info("Hay productos duplicados en tu lista. Revísala bien.")


