import pandas as pd


def filter_list(lista: pd.DataFrame, column: str = "comprar", valor:bool=True):

    return lista[lista[column] == valor]


def clear_selection(data: pd.DataFrame, column: str = "comprar"):
    data[column] = data[column].apply(lambda x: False if x is True else x)


def update_fields(data: pd.DataFrame, new_values: dict, fields: dict):
    filter_col = list(new_values.keys())[0]
    list_new_values = new_values[filter_col]
    for col, value in fields.items():
        data.loc[data[filter_col].isin(list_new_values), [col]] = value


def enter_new_fields(subsetdata: pd.DataFrame, fields_values: dict):
    for col, value in fields_values.items():
        subsetdata[col] = [value]*len(subsetdata)
 

def extract_id_n(id_str: str) -> int:
    numbers = []
    for element in id_str:
        try: 
            numbers.append(int(element))
        except ValueError:
            pass
    
    return int("".join(numbers))
        

def add_id_col(df_main: pd.DataFrame, df_subset: pd.DataFrame, id_colname: str) -> None:
    max_id = extract_id_n(df_main[id_colname].max())
    df_subset[id_colname] = range(max_id + 1, max_id + len(df_subset) + 1)
    df_subset[id_colname] = df_subset[id_colname].apply(lambda x: f"p{x}")


def get_new_elements_in_field(original_df: pd.DataFrame, new_df: pd.DataFrame, field: str) -> dict:
    set_original = set(list(original_df[field].values))
    set_new = set(list(new_df[field].values))
    new_elements = {field : list(set_new - set_original)}
    
    return new_elements