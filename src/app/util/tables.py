class Table():
    COLUMNS = []
    SUB_COLS = []
    DEFAULT = {}
    ID_COL = "id_producto"
    COL_PRODUCTO = "producto"
    backup_path = "src/app/data/backup"

    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name


Productos = Table(file_path="src/app/data/productos.csv",
                  file_name="productos.csv")
Productos.COLUMNS = ["categoría", "id_producto", "producto",
                     "marca", "hay", "comprar"]
Productos.SUB_COLS = ["categoría", "id_producto", "producto",
                     "marca",]
Productos.DEFAULT = {"hay":1, "comprar":False}

# ProductosComprar = Table(file_path="src/app/data/comprar_productos.csv",
#                          file_name="comprar_productos.csv")

Historial = Table(file_path="src/app/data/historial_compras.csv",
                  file_name="historial_compras.csv")
Historial.COLUMNS = ["fecha", "tienda", "categoría", "id_producto",
                     "producto", "marca", "uds_en_paquete", "uds",
                     "kg", "precio_ud", "precio_kg"
                     ]
Historial.SUB_COLS = ["fecha", "tienda", "categoría", "id_producto",
                       "producto", "marca"
                       ]

ProductosEnTiendas = Table(file_path="src/app/data/productos_en_tiendas.csv",
                           file_name="productos_en_tiendas.csv")
ProductosEnTiendas.COLUMNS = ["tienda", "categoría", "id_producto",
                              "producto", "marca", "uds_en_paquete",
                              "uds", "kg", "precio_ud", "precio_kg"
                              ]
ProductosEnTiendas.SUB_COLS = ['id_producto', 'tienda', 'uds_en_paquete',
                                'uds', 'kg', 'precio_ud', 'precio_kg']

# ListaCompra = Table(file_path="src/app/data/listas_compra/",
#                      file_name="")