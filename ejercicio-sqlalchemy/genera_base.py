from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from configuracion import cadena_base_datos
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine(cadena_base_datos)

Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Jugadores(Base):
    __tablename__ = 'jugadores'
    
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    fifa_display = Column(String)
    pais = Column(String)
    apellido = Column(String)
    nombre = Column(String)
    nombre_camiseta = Column(String)
    posicion = Column(String)
    altura = Column(String)
    caps = Column(String)
    goles = Column(String)

    def __repr__(self):
        return "Jugadores: numero: %s fifa_display: %s pais: %s apellido: %s nombre: %s nombre_camiseta: %s posicion: %s altura: %s caps: %s goles: %s" % (
                          self.numero, 
                          self.fifa_display, 
                          self.pais,
                          self.apellido,
                          self.nombre,
                          self.nombre_camiseta,
                          self.posicion,
                          self.altura,
                          self.caps,
                          self.goles)        


Base.metadata.create_all(engine)

