from bo.models import Objetivo, Descripcion

class ObjetivosService(object):
    """
    Servicio para manejar los objetivos.
    """
    
    def __init__(self):
        self._objetivos = []

        obj1 = Objetivo('Objetivo 1')
        obj1.imagen = '/img/G.I.-Joe-Retro-Collection-Storm-Shadow-3.75-inch-Action-Figure-400x600.jpg'

        obj1.descripciones.append(Descripcion('Feria ciruja', 'holocron sublimacion', '$', '10000'))
        obj1.descripciones.append(Descripcion('Retro start', 'RGB', '$', '11000'))
        obj1.descripciones.append(Descripcion('FAA', 'Gameshop', '$', '15000'))

        obj2 = Objetivo('Objetivo 2')
        obj2.imagen = '/img/robot_reloj01.jpg'

        obj2.descripciones.append(Descripcion('Feria ciruja', 'holocron sublimacion', '$', '11000'))
        obj2.descripciones.append(Descripcion('Retro start', 'RGB', '$', '12000'))
        obj2.descripciones.append(Descripcion('FAA', 'Gameshop', '$', '13000'))

        self._objetivos.append(obj1)
        self._objetivos.append(obj2)

    def get_objetivos(self):
        """
        Devuelve la lista de objetivos.
        """
        return self._objetivos
    