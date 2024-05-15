import pandas as pd
import logging
import shutil
from datetime import datetime as dt
import streamlit as st
logging.basicConfig(level=logging.DEBUG)

COLS_HISTORIAL = []
COLS_PRODUCTO = ["categoría", "id_producto", "producto", "marca", "hay", "comprar"]
IND_DESCR_COLS = 5
COL_ID = "id_producto"
COL_PRODUCTO = "producto"

path_historial = "src/app/data/historial_compras_hoy.csv"
path_productos = "src/app/data/productos.csv"
backup_productos = "src/app/data/backup/productos"
path_productos_en_t = "src/app/data/productos_en_tiendas.csv"
save_path = "src/app/data/productos.csv"
processed_path = "src/app/data/processed/historial_compras_timestamp.csv"

def calculate_ids(dataf=pd.DataFrame, id_col=str):
    max_id = dataf[id_col].max()
    max_id = int((max_id.replace("p", "") if max_id and not isinstance(max_id, float) else 0))

    ids = []
    for id_ in range(max_id+1, max_id+len(dataf[id_col])+1):
        ids += [f"p{id_}"]

    return ids


def fill_with_value(df: pd.DataFrame, colname: str, value) -> None:
    length = df.shape[0]
    df[colname] = [value]*length
    

def define_sets(df_historial: pd.DataFrame, df_productos: pd.DataFrame, product_name: str) -> tuple:
    set_productos_historial = set(list(df_historial[product_name].values))
    set_productos = set(list(df_productos[product_name].values))

    return set_productos_historial, set_productos


def extract_new_products(df_historial: pd.DataFrame, df_productos: pd.DataFrame, product_name: str) -> list:
    set_productos_historial, set_productos = define_sets(df_historial, df_productos, product_name)

    return list(set_productos_historial - set_productos)


def extract_bought_products(df_historial: pd.DataFrame, df_productos: pd.DataFrame, product_name: str) -> list:
    set_productos_historial, set_productos = define_sets(df_historial, df_productos, product_name)

    return list(set_productos_historial & set_productos)


# def update_historial_with_ids(df_historial: pd.DataFrame, df_productos: pd.DataFrame, product_name: str) -> None:
#     df_historial_out = df_historial.merge(df_productos, on=product_name)

try:
    productos = pd.read_csv(path_productos, index_col=0, encoding='utf-8')
except FileNotFoundError:
    logging.info("No existen productos registrados. Empezando un nuevo registro...")
    productos = pd.DataFrame(columns=COLS_PRODUCTO)
with st.container():
    edit_productos = st.data_editor(productos,
                num_rows='dynamic',
                use_container_width=True,
                disabled=['producto', 'id_producto'],
                #hide_index=True,
                column_config={
                                        "comprar": st.column_config.CheckboxColumn(
                                            "comprar",
                                            help="Selecciona si quieres comprarme!",
                                            default=False,
                                            )
                                        }
                )

    if st.button("Hacer Lista de la Compra"):
        comprar_df = edit_productos[edit_productos["comprar"] == True]
        comprar_df.to_csv("src/app/data/comprar_productos.csv")
        st.switch_page("pages/lista_de_la_compra.py")

    if st.button("Guardar Productos"):
        shutil.copyfile(path_productos, backup_productos+dt.now().strftime("%Y%m%d%H%M%S"))
        edit_productos.to_csv(path_productos)