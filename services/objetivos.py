from bo.models import Database, Objetivo, Descripcion

class ObjetivosService(object):
    """
    Servicio para manejar los objetivos.
    """
    _instance = None

    def __new__(cls, db_url: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db = Database(db_url)
        return cls._instance

    def get_objetivos(self):
        """
        Devuelve la lista de objetivos.
        """
        with self.db.get_session() as session:
            return session.query(Objetivo).all()
    
    def get_objetivo(self, id: int):
        """
        Devuelve un objetivo por su ID.
        """
        with self.db.get_session() as session:
            return session.get(Objetivo, id)
    
    def save_or_update_objetivo(self, objetivo: Objetivo):
        """
        Guarda un objetivo existente o actualiza uno existente.
        """
        if not isinstance(objetivo, Objetivo):
            raise ValueError("El objetivo debe ser una instancia de la clase Objetivo.")
        
        with self.db.get_session() as session:
            session.add(objetivo)
            session.commit()
            session.refresh(objetivo)
            return objetivo
    