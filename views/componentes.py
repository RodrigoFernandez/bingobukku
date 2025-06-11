from fasthtml.common import *
from services.objetivos import ObjetivosService
from services.usuarios import UsuariosService
from bo.models import Objetivo, Descripcion, Moneda, Usuario
import toml

config = toml.load('bingobukku.toml')

objetivosService = ObjetivosService(config['database']['url'])
usuariosService = UsuariosService(config['database']['url'])
_usr = usuariosService.get_usuario(0)  # Obtener usuario por defecto si no se pasa uno

def get_common_meta():
    return [Meta(charset='utf-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Link(rel='stylesheet', href='/styles/bingobukku.css', type='text/css'),
            Link(rel='icon', href='/img/favicon.png', type='text/css'),]

def get_common_head(titulo='Bingo Bukku', contenido_body=[]):
    contenido_body_final = []
    contenido_body_final.append(Header(titulo, cls='titulo'))
    contenido_body_final += contenido_body
    contenido_body_final.append(Footer('Copyright © 2025', cls='pie'))

    return Head(
        Title(titulo),
        Body(
            tuple(contenido_body_final)
        )
    )

def get_login():
    componentes = get_common_meta()
    componentes.append(Link(rel='stylesheet', href='/styles/login.css', type='text/css'),)
    
    componentes.append(Head(
            Title('Bingo Bukku'),
            Body(
                Container(
                    Div(H1('Bienvenido a Bingo Bukku'), cls='titulo'),
                    Div(
                        Form(
                            Input(id='usuario', type='text', placeholder='Usuario'),
                            Input(id='pass', type='password', placeholder='Contraseña'),
                            Button('Ingresar', id='ingresar'),
                            action='/indice',
                           method='POST'
                        )
                    )
                )
            )
        )
    )

    login = Html(
        tuple(componentes)
    )

    return login

def get_item_objetivo(objetivo):
    return Li(
                A(objetivo.nombre, href=f"/abrir-objetivo/{objetivo.id}"),
            )

def get_indice(usr: Usuario = None):
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/indice.css', type='text/css'))

    # en algun momento se deberia poder pasar un usuario
    print(_usr)
    objetivos = objetivosService.get_objetivos()

    items = [get_item_objetivo(objetivo) for objetivo in objetivos]

    contenido_body_aux=[Container(
                    Div(
                        A('Agregar objetivo', href='/agregar-objetivo'),
                        cls='agregar-objetivo-section'
                    ),
                    Div(
                        Ul(
                        tuple(items),
                        ),
                    cls='objetivos'),
                )]
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))

    return Html(
        tuple(contenidos),
    )

def get_agregar_objetivo():
    print(_usr)
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/objetivo.css', type='text/css'))
    contenido_body_aux = [
                Section(
                    Form(
                        Input(id='objetivo', type='text', placeholder='Objetivo'),
                        Br(),
                        Div(
                            Button('Aceptar', id='aceptar'),
                            Button('Cancelar', id='cancelar', type='reset', onclick=f"window.location.href='/indice';"),
                        ),
                        action='/nuevo-objetivo',
                        method='POST'
                    ),
                    cls='objetivo-form'
                )]
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))
    
    return Html(
        tuple(contenidos)
    )

def add_nuevo_objetivo(data: dict):
    """
    Agrega un nuevo objetivo a la lista de objetivos.
    """
    
    nuevo_obj = Objetivo(
        id=None,  # El ID se asignará automáticamente
        nombre=data.get('objetivo', '').strip(),
        usuario_id=_usr.id,
        usuario=_usr)
    
    objetivosService.save_or_update_objetivo(nuevo_obj)
    # Redirigir al índice después de agregar el objetivo
    return get_indice(_usr)

def get_titulo_link_descripcion(descripcion):    
    return " | ".join([descripcion.feria, descripcion.local, f"{descripcion.moneda}{descripcion.precio}"])

def get_item_descripcion(descripcion):
    return Li(
                A(get_titulo_link_descripcion(descripcion), href=f"/mostrar-descripcion/{descripcion.id}"),
                A('X', cls='borrar-descripcion')
            )
    
def get_abrir_objetivo(id: int):
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/objetivo.css', type='text/css'))

    objetivo = objetivosService.get_objetivo(id)
    items = [get_item_descripcion(descripcion) for descripcion in objetivo.descripciones]
    ruta_imagen = objetivo.imagen

    contenido_body_aux = [Header(
                    Div(),
                    Div(objetivo.nombre),
                    Div(A('Volver', href='/indice')),
                    cls='objetivo-header'
                    ),
                Container(
                    Div(
                        Img(src=ruta_imagen, alt='Imagen Objetivo', cls='objetivo-img'),
                        cls='objetivo-imgs'
                    ),
                    Div(
                        Ul(
                            tuple(items)
                        ),
                       cls='descripciones'),
                    Div(
                        A('Agregar descripcion', href=f"/agregar-descripcion/{objetivo.id}", cls='agregar-descripcion'),
                        cls='agregar-descripcion-section'
                        ),
                )]
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))

    return Html(
        tuple(contenidos)
    )

def get_agregar_descripcion(objetivo_id: int):
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/descripcion.css', type='text/css'))
    contenido_body_aux=[
                Section(
                    Form(
                        Input(id='objetivo_id', type='text', placeholder='objetivo_id', value=objetivo_id, hidden=True),
                        Input(id='local', type='text', placeholder='Local'),
                        Br(),
                        Input(id='feria', type='text', placeholder='Feria'),
                        Br(),
                        Div(
                            Select(id='moneda', placeholder='Moneda')(
                                Option(Moneda.PESOS.value, value=Moneda.PESOS.name, selected=True),
                                Option(Moneda.DOLARES.value, value=Moneda.DOLARES.name),
                            ),
                            Input(id='precio', type='number', placeholder='Precio'),
                            cls='precio-select'
                        ),
                        Textarea(id='comentario', placeholder='Comentario'),
                        Br(),
                        Div(
                            Button('Agregar', id='agregar'),
                            Button('Cancelar', id='cancelar', type='reset', onclick=f"window.location.href='/abrir-objetivo/{objetivo_id}';"),
                            cls='botonera-descripcion'
                        ),
                        action='/nueva-descripcion',
                        method='POST'
                    ),
                    cls='descripcion-form'
                )]
    
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))
    return Html(
        tuple(contenidos)
    )

def add_nueva_descripcion(data: dict):
    """
    Agrega una nueva descripción a un objetivo.
    """
    print(data)
    objetivo_id = int(data.get('objetivo_id', 0))
    feria = data.get('feria', '').strip()
    local = data.get('local', '').strip()
    moneda = data.get('moneda', Moneda.PESOS.name)
    moneda = Moneda.get_value(moneda)
    precio = data.get('precio', '').strip()
    
    #if not objetivo_id or not feria or not local or not precio:
    #    return get_agregar_descripcion()  # Retorna el formulario si faltan datos

    descripcion = Descripcion(
        id=None,  # El ID se asignará automáticamente
        feria=feria,
        local=local,
        moneda=moneda,
        precio=precio
    )
    
    objetivo = objetivosService.get_objetivo(objetivo_id)
    if objetivo:
        objetivo.descripciones.append(descripcion)
        objetivosService.save_or_update_objetivo(objetivo)

    # Redirigir al objetivo después de agregar la descripción
    return get_abrir_objetivo(objetivo_id)

def get_mostrar_descripcion(id: int):
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/descripcion.css', type='text/css'))

    descripcion = objetivosService.get_descripcion(id)
    if not descripcion:
        return Html("Descripción no encontrada", status=404)

    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/descripcion.css', type='text/css'))
    contenido_body_aux = [Div(f"Esto es una prueba: {descripcion.id}")]
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))

    return Html(
        tuple(contenidos)
    )
