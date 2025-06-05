from enum import Enum

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

class Objetivo(object):
    """
    Objetivo buscado.
    """
    def __init__(self, id: int, nombre: str):
        self.__id = id
        self._nombre = nombre
        self._descripciones = []
        self._imagen = None

    @property
    def id(self) -> int:
        """
        Devuelve el ID del objetivo.
        """
        return self.__id
    
    @id.setter
    def id(self, id: int):
        """
        Establece el ID del objetivo.
        """
        self.__id = id

    @property
    def nombre(self) -> str:
        """
        Devuelve el nombre del objetivo.
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        """
        Establece el nombre del objetivo.
        """
        self._nombre = nombre
    
    @property
    def descripciones(self) -> list:
        """
        Devuelve las descripciones del objetivo.
        """
        return self._descripciones
    
    @descripciones.setter
    def descripciones(self, descripciones: list):
        """
        Establece las descripciones del objetivo.
        """
        self._descripciones = descripciones
    
    @property
    def imagen(self) -> str:
        """
        Devuelve la imagen del objetivo.
        """
        return self._imagen
    
    @imagen.setter
    def imagen(self, imagen: str):
        """
        Establece la imagen del objetivo.
        """
        self._imagen = imagen
    
    def __repr__(self):
        """
        Representación del objetivo.
        """
        return f"Objetivo(id={self.__id}, nombre={self._nombre}, descripciones={len(self._descripciones)}, imagen={self._imagen})"

class Descripcion(object):
    """
    Descripción de un objetivo.
    """
    def __init__(self, id: int, feria: str, local: str, moneda: str, precio: str, objetivo_id: int = None):
        self.__id = id
        self._feria = feria
        self._local = local
        self._moneda = moneda
        self._precio = precio
        self._objetivo_id = objetivo_id

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id
    
    @property
    def feria(self) -> str:
        return self._feria
    
    @feria.setter
    def feria(self, feria: str):
        self._feria = feria
    
    @property
    def local(self) -> str:
        return self._local
    
    @local.setter
    def local(self, local: str):
        self._local = local
    
    @property
    def moneda(self) -> str:
        return self._moneda
    
    @moneda.setter
    def moneda(self, moneda: str):
        self._moneda = moneda

    @property
    def precio(self) -> str:
        return self._precio
    
    @precio.setter
    def precio(self, precio: str):
        self._precio = precio
    
    @property
    def objetivo_id(self) -> str:
        return self._objetivo_id
    
    @objetivo_id.setter
    def objetivo_id(self, objetivo_id: int):
        self._objetivo_id = objetivo_id
    
    def __repr__(self):
        return f"Descripcion(id={self.__id},feria={self._feria}, local={self._local}, moneda={self._moneda}, precio={self._precio}, objetivo_id={self._objetivo_id})"
