from enum import Enum
from sqlmodel import SQLModel, create_engine, Session, Field, Relationship

class Moneda(Enum):
    """
    Enum para las monedas.
    """
    PESOS = '$'
    DOLARES = 'u$d'

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]
    
    @classmethod
    def get_value(cls, name: str):
        return cls[name].value if name in cls.__members__ else None

class Usuario(SQLModel, table=True):
    """
    Usuario del sistema.
    """
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(default='', nullable=False)
    mail: str = Field(default='', nullable=False)
    password: str = Field(default='', nullable=False)
    objetivos: list['Objetivo'] = Relationship(back_populates='usuario')
    
class Objetivo(SQLModel, table=True):
    """
    Objetivo buscado.
    """
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(default='', nullable=False)
    descripciones: list['Descripcion'] = Relationship(back_populates='objetivo')
    imagen: str | None = Field(nullable=True, default=None)
    usuario_id: int = Field(foreign_key='usuario.id', nullable=False)
    usuario: Usuario = Relationship(back_populates='objetivos')

class Descripcion(SQLModel, table=True):
    """
    Descripción de un objetivo.
    """
    id: int | None = Field(default=None, primary_key=True)
    feria: str = Field(default='', nullable=False)
    local: str = Field(default='', nullable=False)
    moneda: str = Field(default='PESOS', nullable=False)
    precio: float = Field(default=0.0, nullable=False)
    objetivo_id: int = Field(foreign_key='objetivo.id', nullable=False)
    objetivo: Objetivo = Relationship(back_populates='descripciones')


class Database:
    _instance = None

    def __new__(cls, db_url: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.engine = create_engine(db_url)
        return cls._instance
    
    def get_session(self):
        return Session(self.engine)
    
def crear_db(sqlite_url):
    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    import toml
    config = toml.load('bingobukku.toml')
    
    crear_db(config['database']['url'])
    