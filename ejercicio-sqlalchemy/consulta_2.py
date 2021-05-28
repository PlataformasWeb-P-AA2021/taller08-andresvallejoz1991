from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_base import Jugadores 

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad docentes 
jugadores = session.query(Jugadores).all()


# Obtener todos los registros de 
# la tabla docentes que tengan como valor en 
# el atributo especifico 
jugadores_dos = session.query(Jugadores).order_by(Jugadores.altura).all()
print(jugadores_dos)