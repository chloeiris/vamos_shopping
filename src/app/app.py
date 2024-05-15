import logging
import pandas as pd
import streamlit as st

from productos import extract_new_products, calculate_ids, fill_with_value, extract_bought_products

logging.basicConfig(level=logging.DEBUG)

COLS_HISTORIAL = []
COLS_PRODUCTO = ["categoría", "id_producto", "producto", "marca", "hay", "comprar"]
IND_DESCR_COLS = 5
COL_ID = "id_producto"
COL_PRODUCTO = "producto"

path_historial="src/app/data/historial_compras_hoy.csv"
path_productos="src/app/data/productos.csv"
path_productos_en_t="src/app/data/productos_en_tiendas.csv"
save_path="src/app/data/productos.csv"
processed_path="src/app/data/processed/historial_compras_timestamp.csv"

st.sidebar.write("Vamos Shopping!")
if st.sidebar.button("Productos"):
    try:
        productos = pd.read_csv(path_productos, index_col=0, encoding='utf-8')
    except FileNotFoundError:
        logging.info("No existen productos registrados. Empezando un nuevo registro...")
        productos = pd.DataFrame(columns=COLS_PRODUCTO)
    
    edit_productos = st.data_editor(productos, num_rows='dynamic', hide_index=True, )

    if st.button("Hacer Lista de la Compra"):
        comprar_df = edit_productos[edit_productos["comprar"] is True]
        productos_en_tiendas = pd.read_csv(path_productos_en_t, index_col=0, encoding='utf-8')
        if comprar_df.duplicated().sum() == 0:
            lista_compra = comprar_df.merge(productos_en_tiendas, on="id_producto", how="left")
            logging.info("Lista de la compra calculada!")
            #TODO: redireccionar a pestaña
        logging.info("Hay productos duplicados en tu lista. Revísala bien.")
    # Mostrar el df y un checkbox para marcar lo que hay que comprar
    # Filtrar por True y guardar en otra variable
    # Poner un boton de "Hacer lista de la compra"
    # Redirecciona a Lista de la compra y hace el join con productos en tiendas
    # Hay un botón de Añadir producto - le calcula el id y lo marca como comprar
# if st.sidebar.button("Lista de la Compra"):
#     # Muestra la lista calculada con casillas para marcar lo que ha comprado
#     # Permite editar lo que esta marcado en la lista para cambiar cantidades precios o tiendas y actualizar el historial y productos en tiendas
#     # Boton para guardar en historial y actualizar productos en tiendas
#     # Mensaje de que se ha guardado correctamente
# if st.sidebar.button("Productos en Tiendas"):
#     # Muestra los datos obtenidos del historial
#     # Permite eliminar registros
#     # Se guarda un backup antes de cada actualización
# if st.sidebar.button("Tiendas"):
#     # Muestra la lista
#     # Permite añadir registros
#     # Se actualiza con el historial nuevo
# if st.sidebar.button("Historial"):
#     # Muestra todo el historial, se podrán ver stats
#     # Se guarda un backup de cada compra


# try:
#     historial_compras = pd.read_csv(path_historial, encoding='utf-8')
# except FileNotFoundError as exc:
#     raise FileNotFoundError("Historial de compras no encontrado") from exc

# try:
#     productos = pd.read_csv(path_productos, index_col=0)
# except FileNotFoundError:
#     logging.info("No existen productos registrados. Empezando un nuevo registro...")
#     productos = pd.DataFrame(columns=COLS_PRODUCTO)

# # TODO filtrar historial por fecha
# add_productos = extract_new_products(historial_compras, productos, COL_PRODUCTO)

# if add_productos:
#     productos_nuevos = historial_compras[historial_compras[COL_PRODUCTO].isin(add_productos)]
#     productos_nuevos.drop_duplicates(COL_PRODUCTO, inplace=True)

#     dict_productos_nuevos = {}
#     for col in COLS_PRODUCTO[:IND_DESCR_COLS]:
#         if col == COL_ID:
#             dict_productos_nuevos[COL_ID] = calculate_ids(productos, COL_ID)
#             logging.debug("Ids calculados")
#         dict_productos_nuevos[col] = tuple(productos_nuevos[col].values)

#     productos_nuevos_df = pd.DataFrame(dict_productos_nuevos)

#     for col in COLS_PRODUCTO[IND_DESCR_COLS:]:
#         fill_with_value(productos_nuevos_df, col[0], col[1])
    
#     logging.info("Se van a añadir %s productos nuevos al registro", productos_nuevos_df.shape[0])
#     logging.debug("""
#                     -----------------
#                     Dataframe productos nuevos:
#                     %s""", productos_nuevos_df.head() )

#     productos = pd.concat([productos, productos_nuevos_df])

# productos_comprados = extract_bought_products(historial_compras, productos, COL_PRODUCTO)

# if productos_comprados:
#     comprados = productos[productos[COL_PRODUCTO].isin(productos_comprados)]
#     logging.debug("""
#                     -----------------
#                     Dataframe productos comprados:
#                     %s""", comprados.head())
    
#     for col in COLS_PRODUCTO[IND_DESCR_COLS:]:
#         fill_with_value(comprados, col[0], col[1])
#     logging.info("%s productos ya registrados marcados como comprados", comprados.shape[0])
# logging.info("No ha habido productos ya registrados comprados")

# productos.to_csv(save_path)


# # if __name__ == "__main__":
# # main()
