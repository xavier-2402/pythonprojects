import sqlalchemy as db
import pandas

class Conexion:
    def __init__(self):
        super().__init__()
        self.conectar()

    def conectar(self):

        #Creamos la cedena de conexión
        nombreusuario="root"
        password=""
        servidor:"localhost"
        puerto:"3306"
        base_datos="crudpython"

        engine= db.create_engine(f"mysql+mysqlconnector://{nombreusuario}:{password}@{servidor}:{puerto}/{base_datos}",echo=True)
        #Conectamos a la DB
        self.connection = engine.connect()
        print(self.connection)
        #Mapeo de la información de DB
        metadata= db.MetaData()

        self.usuarios = db.Table('usuario',metadata = metadata, autoload = True,autoload_with = engine)

        self.vehiculos = db.Table('vehiculos',metadata = metadata, autoload = True,autoload_with = engine)


conexion = Conexion()
         