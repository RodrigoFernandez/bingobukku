from bo.models import Database, Usuario

class UsuariosService(object):
    """
    Servicio para manejar los usuarios.
    """
    _instance = None

    def __new__(cls, db_url: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db = Database(db_url)
        return cls._instance

    def __init__(self, db_url: str):
        self.db = Database(db_url)

    def get_usuario(self, id: int):
        """
        Devuelve un usuario por su ID.
        """
        with self.db.get_session() as session:
            return session.get(Usuario, id)

    def add_usuario(self, usuario: Usuario):
        """
        Agrega un nuevo usuario a la base de datos.
        """
        with self.db.get_session() as session:
            session.add(usuario)
            session.commit()
            session.refresh(usuario)
            return usuario

    def validar_login(self, username: str, password: str):
        pass
