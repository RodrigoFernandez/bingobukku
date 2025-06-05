from bo.models import Objetivo, Descripcion

class ObjetivosService(object):
    """
    Servicio para manejar los objetivos.
    """
    
    def __init__(self):
        self._objetivos = []

        obj1 = Objetivo(1, 'Objetivo 1')
        obj1.imagen = '/img/G.I.-Joe-Retro-Collection-Storm-Shadow-3.75-inch-Action-Figure-400x600.jpg'

        obj1.descripciones.append(Descripcion(1, 'Feria ciruja', 'holocron sublimacion', '$', '10000'))
        obj1.descripciones.append(Descripcion(2, 'Retro start', 'RGB', '$', '11000'))
        obj1.descripciones.append(Descripcion(3, 'FAA', 'Gameshop', '$', '15000'))

        obj2 = Objetivo(2, 'Objetivo 2')
        obj2.imagen = '/img/robot_reloj01.jpg'

        obj2.descripciones.append(Descripcion(1, 'Feria ciruja', 'holocron sublimacion', '$', '11000'))
        obj2.descripciones.append(Descripcion(2, 'Retro start', 'RGB', '$', '12000'))
        obj2.descripciones.append(Descripcion(3, 'FAA', 'Gameshop', '$', '13000'))

        self._objetivos.append(obj1)
        self._objetivos.append(obj2)

    def get_objetivos(self):
        """
        Devuelve la lista de objetivos.
        """
        return self._objetivos
    
    def get_objetivo(self, id: int):
        """
        Devuelve un objetivo por su ID.
        """
        for obj in self._objetivos:
            if obj.id == id:
                return obj
        return None
    
    def add_objetivo(self, objetivo: Objetivo):
        """
        Agrega un nuevo objetivo a la lista de objetivos.
        """
        if not isinstance(objetivo, Objetivo):
            raise ValueError("El objetivo debe ser una instancia de la clase Objetivo.")
        
        objetivo.id = len(self._objetivos) + 1  # Asigna un nuevo ID basado en la longitud actual
        self._objetivos.append(objetivo)

    def guardar_objetivo(self, objetivo: Objetivo):
        """
        Guarda un objetivo existente o actualiza uno existente.
        """
        if not isinstance(objetivo, Objetivo):
            raise ValueError("El objetivo debe ser una instancia de la clase Objetivo.")
        
        for i, obj in enumerate(self._objetivos):
            if obj.id == objetivo.id:
                self._objetivos[i] = objetivo
                return
        
        # Si no se encontró el objetivo, lo agrega como nuevo
        self.add_objetivo(objetivo)
    