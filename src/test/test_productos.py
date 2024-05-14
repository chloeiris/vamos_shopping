import unittest
from unittest.mock import patch
from app.productos import calculate_ids, main


## calculate_ids
# happy path: max_id es p46
# happy path: max_id es nan
# unhappy path: max_id es 0
# unhappy path: max_id es "p"
# unhappy path: id_col can't be found/ similar error


## main
# HAPPY PATH:
# - Los ficheros se leen correctamente
# - No salta el FileNorFoundError, sino que se genera un df vacio
# - add_productos es una lista vacía
# - add_productos es una lista llena
# - productos_comprados es una lista vacía
# - productos_comprados es una lista llena

# UNHAPPY PATH:
# - Salta el error de que no ecuentra el historial
# - La columna producto no existe en los df leidos.
# - add_prodcutos es un np.NaN o un None
# - productos_comprados es un np.NaN o un None


class TestApp(unittest.TestCase):
    """_summary_ class of unit tests
    """

    def setUp(self) -> None:
        """_summary_ setup connections
        """
        self.session = boto3.session.Session()
        self.client = self.session.client(
            service_name="secretsmanager", region_name="eu-west-2"
        )
    
    @patch
    def test_list_source_files(self) -> None:
        """_summary_ test example
        """
        ## arrange
        ## act
        ## assert

        self.assertEqual(1, 1)



if __name__ == "__main__":
    unittest.main()
