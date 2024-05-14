import pandas as pd
import logging
logging.basicConfig(level=logging.DEBUG)


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


