import logging
import pandas as pd
import streamlit as st
from util.tables import Productos
from util.transformations import clear_selection, enter_new_fields
from util.os_ops import save_backup

logging.basicConfig(level=logging.DEBUG)


try:
    productos = pd.read_csv(Productos.file_path, index_col=0, encoding="utf-8")
except FileNotFoundError:
    logging.info("No existen productos registrados. Empezando un nuevo registro...")
    productos = pd.DataFrame(columns=Productos.COLUMNS)

with st.container():
    st.header("Productos")
    st.button("Limpiar Selección", on_click=clear_selection(productos))

    edit_productos = st.data_editor(
        productos,
        num_rows='dynamic',
        use_container_width=True,
        # disabled=['producto', 'id_producto'],
        # hide_index=True,
        column_config={
            "comprar": st.column_config.CheckboxColumn(
                "comprar",
                help="Selecciona si quieres comprarme!",
                default=False,
                ),
            "categoría": st.column_config.SelectboxColumn(
                "categoría",
                default="Nuevo"
                options=list(productos["categoría"].unique())
            )
            }
                                    )

    if st.button("Hacer Lista de la Compra"):
        save_backup(Productos.file_path,
                    Productos.backup_path,
                    Productos.file_name)
        edit_productos.to_csv(Productos.file_path, encoding="utf-8")
        st.switch_page("pages/lista_de_la_compra.py")      

    if len(productos) != len(edit_productos):
        if len(edit_productos) > len(productos):
            set_productos = set(list(productos[Productos.COL_PRODUCTO].values))
            set_edit_productos = set(list(edit_productos[Productos.COL_PRODUCTO].values))
            new_productos = list(set_edit_productos - set_productos)
            
            fields_to_calculate =  edit_
            enter_new_fields()
            # TODO add new ids for new records

        st.button("Guardar Cambios",
                  on_click=edit_productos.to_csv(Productos.file_path))