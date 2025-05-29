from fasthtml.common import *
from services.objetivos import ObjetivosService

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
                A(objetivo.nombre, href='/abrir-objetivo')
            )

def get_indice():
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/indice.css', type='text/css'))

    objetivosService = ObjetivosService()
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
    contenido_body_aux = [Form(
                    Input(id='Objetivo', type='text', placeholder='Objetivo'),
                    Button('Aceptar', id='aceptar'),
                    Button('Cancelar', id='cancelar', hx_get='/indice', hx_target='#contenido'),
                    action='/indice',
                    method='POST'
                )]
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))
    
    return Html(
        tuple(contenidos)
    )

def get_titulo_link_descripcion(descripcion):    
    return " | ".join([descripcion.feria, descripcion.local, descripcion.moneda + descripcion.precio])

def get_item_descripcion(descripcion):
    return Li(
                A(get_titulo_link_descripcion(descripcion), href='/mostrar-descripcion'),
                A('X', cls='borrar-descripcion')
            )
    
def get_abrir_objetivo():
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/objetivo.css', type='text/css'))

    objetivosService = ObjetivosService()
    objetivo = objetivosService.get_objetivos()[0]
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
                    A('Agregar descripcion', href='/agregar-descripcion'),
                )]
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))

    return Html(
        tuple(contenidos)
    )

def get_agregar_descripcion():
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/descripcion.css', type='text/css'))
    contenido_body_aux=[
                Section(
                    Form(
                        Input(id='Feria', type='text', placeholder='Feria'),
                        Br(),
                        Input(id='Local', type='text', placeholder='Local'),
                        Br(),
                        Div(
                            Select(id='Moneda', placeholder='Moneda')(
                                Option('$', value='pesos', selected=True),
                                Option('u$d', value='dolares'),
                            ),
                            Input(id='Precio', type='number', placeholder='Precio'),
                            cls='precio-select'
                        ),
                        Textarea(id='Comentario', placeholder='Comentario'),
                        Br(),
                        Div(
                            Button('Agregar', id='agregar'),
                            Button('Cancelar', id='cancelar', hx_get='/abrir-objetivo'),
                            cls='botonera-descripcion'
                        ),
                        action='/abrir-objetivo',
                        method='POST'
                    ),
                    cls='descripcion-form'
                )]
    
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))
    return Html(
        tuple(contenidos)
    )
