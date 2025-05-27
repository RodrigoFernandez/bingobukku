from fasthtml.common import *
from views.componentes import get_login, get_indice, get_agregar_objetivo, get_abrir_objetivo, get_agregar_descripcion

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

@rt('/abrir-objetivo') 
def abrir_objetivo():
    return get_abrir_objetivo()

@rt('/agregar-descripcion')
def agregar_descripcion():
    return get_agregar_descripcion()

serve()
