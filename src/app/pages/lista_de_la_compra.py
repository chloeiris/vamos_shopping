from datetime import datetime as dt
import pandas as pd
import streamlit as st
import logging
from util.tables import Productos, ProductosEnTiendas, Historial
from util.transformations import filter_list, get_new_elements_in_field, add_id_col, enter_new_fields
from util.os_ops import save_backup

logging.basicConfig(level=logging.DEBUG)


with st.container():
    st.header("Lista de la Compra")

    productos = pd.read_csv(Productos.file_path, index_col=0, encoding="utf-8")[Productos.SUB_COLS]
    if productos.duplicated().sum() == 0:
        productos_comprar = filter_list(productos)
        productos_en_tiendas = pd.read_csv(ProductosEnTiendas.file_path, index_col=0, encoding="utf-8")[ProductosEnTiendas.SUB_COLS]
        lista_compra = productos_comprar.merge(productos_en_tiendas, on=Productos.ID_COL, how="left").drop(Productos.ID_COL, axis=1)
        lista_compra.insert(0, "comprado", [False]*lista_compra.shape[0])
        st.write("Lista de la compra calculada!")

        lista_compra_edit = st.data_editor(
            lista_compra,
            use_container_width=True,
            num_rows='dynamic'
                                            )
    else:
        st.write("Hay productos duplicados en tu lista. Revísala bien.")
        st.button("Mostrar Duplicados", on_click=st.write(productos.duplicated().values))
        #TODO: validar insercion de datos

    st.write("Compra hecha? Actualiza el historial para aprovechar los datos!")

    if st.button("Actualizar historial"):
        productos = pd.read_csv(Productos.file_path, index_col=0, encoding='utf-8')
        historial_compras = pd.read_csv(Historial.file_path, index_col=0, encoding='utf-8')
        productos_en_tiendas = pd.read_csv(ProductosEnTiendas.file_path, index_col=0, encoding='utf-8')
        productos_comprados = filter_list(lista=lista_compra_edit, column="comprado").drop("comprado", axis=1)

        set_productos = set(list(productos[Productos.COL_PRODUCTO].values))
        set_comprados = set(list(productos_comprados[Productos.COL_PRODUCTO].values))
        new_productos = list(set_productos.difference(set_comprados))

        new_productos_df = lista_compra_edit[lista_compra_edit[Productos.COL_PRODUCTO].isin(new_productos)][["categoría", "producto", "marca"]]
        add_id_col(productos, new_productos_df, Productos.ID_COL)
        
        enter_new_fields(new_productos_df, Productos.DEFAULT)


        new_productos = get_new_elements_in_field(productos, lista_compra_edit, Productos.COL_PRODUCTO)




        # historial_last = filter_list(lista=lista_compra_edit, column="comprado").drop("comprado", axis=1)
        # historial_last.insert(0, "fecha", [dt.now().strftime("%d/%m/%Y")]*len(historial_last))
        # historial = pd.concat([historial_compras, historial_last], ignore_index=True))
        # save_backup(path_historial, path_backup, historial_csv)
        # historial.to_csv(path_historial, encoding='utf-8')

        
        # productos_en_tiendas_last = historial_last.groupby(['tienda', 'categoría', 'id_producto', 'producto', 'marca']).max("fecha").reset_index()
        # p_en_t = pd.concat([productos_en_tiendas, productos_en_tiendas_last], ignore_index=True)
        # p_en_t.drop_duplicates(['tienda', 'categoría', 'id_producto', 'producto'], keep="last", inplace=True)
        # save_backup(path_productos_en_t, path_backup, productos_en_t_csv)
        # p_en_t.to_csv(path_productos_en_t, encoding='utf-8')

        
        # if historial_last["id_producto"].isnull().sum() 







