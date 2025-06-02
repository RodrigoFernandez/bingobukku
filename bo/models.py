
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
    def __init__(self, id: int, feria: str, local: str, moneda: str, precio: str):
        self.__id = id
        self._feria = feria
        self._local = local
        self._moneda = moneda
        self._precio = precio

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id
    
    @property
    def feria(self) -> str:
        return self._feria
    
    @property
    def local(self) -> str:
        return self._local
    
    @property
    def moneda(self) -> str:
        return self._moneda
    
    @property
    def precio(self) -> str:
        return self._precio
    
    def __repr__(self):
        return f"Descripcion(id={self.__id},feria={self._feria}, local={self._local}, moneda={self._moneda}, precio={self._precio})"
