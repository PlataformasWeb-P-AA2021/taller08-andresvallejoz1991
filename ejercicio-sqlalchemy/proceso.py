from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_base import Jugadores

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Apertura del Archivo
files = open("data/mundial2018.csv", "r", encoding="utf8")
#Lectura del archivo
datos_clubes = files.readlines()

#Ingreso de datos 
for i in range(0,len(datos_clubes),1):
        d=datos_clubes[i].split("|")
        p = Jugadores(numero=d[0], fifa_display=d[1],pais=d[2],apellido=d[3],nombre=d[4],nombre_camiseta=d[5],posicion=d[6],altura=d[7],caps=d[8],goles=d[9])
        session.add(p)
#Cierre del archivo
files.close()

# se confirma las transacciones
session.commit()
