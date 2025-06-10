from fasthtml.common import *
from views.componentes import get_login, get_indice, get_agregar_objetivo, get_abrir_objetivo, get_agregar_descripcion, add_nuevo_objetivo, add_nueva_descripcion
import toml
from bo.models import Database


config = toml.load('bingobukku.toml')
print(f"Configuración cargada: {config}")

db = Database(config['database']['url'])

app, rt = fast_app(
                live=True,
                pico=False,
                static_path='statics'
            )

@rt('/')
def get():
    return get_login()

@rt('/indice')
def index():
    return get_indice()

@rt('/agregar-objetivo')
def agregar_objetivo():
    return get_agregar_objetivo()

@rt('/nuevo-objetivo', methods=['POST'])
def nuevo_objetivo(data: dict):
    return add_nuevo_objetivo(data)

@rt('/abrir-objetivo/{id}') 
def abrir_objetivo(id: int):
    return get_abrir_objetivo(id)

@rt('/agregar-descripcion/{objetivo_id}')
def agregar_descripcion(objetivo_id: int):
    return get_agregar_descripcion(objetivo_id)

@rt('/nueva-descripcion', methods=['POST'])
def nueva_descripcion(data: dict):
    return add_nueva_descripcion(data)

serve()
