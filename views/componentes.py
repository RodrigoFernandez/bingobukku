from fasthtml.common import *
from services.objetivos import ObjetivosService
from bo.models import Objetivo, Descripcion

objetivosService = ObjetivosService()

def get_common_meta():
    return [Meta(charset='utf-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Link(rel='stylesheet', href='/styles/bingobukku.css', type='text/css'),
            Link(rel='icon', href='/img/favicon.png', type='text/css'),]

def get_common_head(titulo='Bingo Bukku', contenido_body=[]):
    contenido_body_final = []
    contenido_body_final.append(Header(titulo, cls='titulo'))
    contenido_body_final += contenido_body
    contenido_body_final.append(Footer(Span('Copyright © 2025')))

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
                A(objetivo.nombre, href='/abrir-objetivo/' + str(objetivo.id)),
            )

def get_indice():
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/indice.css', type='text/css'))

    
    objetivos = objetivosService.get_objetivos()

    items = [get_item_objetivo(objetivo) for objetivo in objetivos]

    contenido_body_aux=[Container(
                    A('Agregar objetivo', href='/agregar-objetivo'),
                    Div(
                        tuple(items),
                    cls='objetivos'),
                )]
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))

    return Html(
        tuple(contenidos),
    )

def get_agregar_objetivo():
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/objetivo.css', type='text/css'))
    contenido_body_aux = [
                Section(
                    Form(
                        Input(id='objetivo', type='text', placeholder='Objetivo'),
                        Br(),
                        Div(
                            Button('Aceptar', id='aceptar'),
                            Button('Cancelar', id='cancelar', hx_get='/indice', hx_target='#contenido'),
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
    print(data)
    print(data.get('objetivo', '').strip())
    nuevo_obj = Objetivo(
        id=None,  # El ID se asignará automáticamente
        nombre=data.get('objetivo', '').strip())
    
    objetivosService.add_objetivo(nuevo_obj)
    # Redirigir al índice después de agregar el objetivo
    return get_indice()

def get_titulo_link_descripcion(descripcion):    
    return " | ".join([descripcion.feria, descripcion.local, descripcion.moneda + descripcion.precio])

def get_item_descripcion(descripcion):
    return Li(
                A(get_titulo_link_descripcion(descripcion), href='/mostrar-descripcion'),
                A('X', cls='borrar-descripcion')
            )
    
def get_abrir_objetivo(id: int):
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/objetivo.css', type='text/css'))

    objetivo = objetivosService.get_objetivo(id)

    print(objetivo)
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
                        Img(src=ruta_imagen, alt='Objetivo', cls='objetivo-img'),
                        cls='objetivo-imgs'
                    ),
                    Div(tuple(items),
                       cls='descripciones'),
                    A('Agregar descripcion', href='/agregar-descripcion/' + str(objetivo.id), cls='agregar-descripcion'),
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
                        Input(id='feria', type='text', placeholder='Feria'),
                        Br(),
                        Input(id='local', type='text', placeholder='Local'),
                        Br(),
                        Div(
                            Select(id='moneda', placeholder='Moneda')(
                                Option('$', value='pesos', selected=True),
                                Option('u$d', value='dolares'),
                            ),
                            Input(id='precio', type='number', placeholder='Precio'),
                            cls='precio-select'
                        ),
                        Textarea(id='comentario', placeholder='Comentario'),
                        Br(),
                        Div(
                            Button('Agregar', id='agregar'),
                            Button('Cancelar', id='cancelar', hx_get='/abrir-objetivo'),
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
    #feria = data.get('Feria', '').strip()
    #local = data.get('Local', '').strip()
    #moneda = data.get('Moneda', 'pesos')
    #precio = data.get('Precio', '').strip()
    
    #if not objetivo_id or not feria or not local or not precio:
    #    return get_agregar_descripcion()  # Retorna el formulario si faltan datos

    #descripcion = Descripcion(
    #    id=None,  # El ID se asignará automáticamente
    #    feria=feria,
    #    local=local,
    #    moneda=moneda,
    #    precio=precio
    #)
    
    #objetivo = objetivosService.get_objetivo(objetivo_id)
    #if objetivo:
    #    objetivo.descripciones.append(descripcion)
    
    # Redirigir al objetivo después de agregar la descripción
    return get_abrir_objetivo(objetivo_id)