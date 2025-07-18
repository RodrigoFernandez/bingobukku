from fasthtml.common import *
from views.componentes import add_img_objetivo, get_login, get_indice, get_agregar_objetivo, get_abrir_objetivo, get_agregar_descripcion, add_nuevo_objetivo, add_nueva_descripcion, get_mostrar_descripcion, get_registro_alta, add_nuevo_usuario, get_subir_img_objetivo
import toml
from bo.models import Database


config = toml.load('bingobukku.toml')

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

@rt('/mostrar-descripcion/{id}')
def mostrar_descripcion(id: int):
    return get_mostrar_descripcion(id)

@rt('/subir-img-objetivo/{objetivo_id}')
def subir_img_objetivo(objetivo_id: int):
    return get_subir_img_objetivo(objetivo_id)

@rt('/agregar-imagen-objetivo', methods=['POST'])
async def agregar_imagen_objetivo(data: dict):
    return await add_img_objetivo(data)

@rt('/registro_alta')
def registro_alta():
    return get_registro_alta()

@rt('/nuevo-usuario', methods=['POST'])
def nuevo_usuario(data: dict):
    return add_nuevo_usuario(data)

serve()
