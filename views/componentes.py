from fasthtml.common import *

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

def get_indice():
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/indice.css', type='text/css'))

    contenido_body_aux=[Container(
                    A('Agregar objetivo', href='/agregar-objetivo'),
                    Div(
                        Li(
                            A('Objetivo 1', href='/abrir-objetivo')
                        ),
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

def get_abrir_objetivo():
    contenidos = get_common_meta()
    contenidos.append(Link(rel='stylesheet', href='/styles/objetivo.css', type='text/css'))
    contenido_body_aux = [Header(
                    Div(),
                    Div('Objetivo 1'),
                    Div(A('Volver', href='/indice')),
                    cls='objetivo-header'
                    ),
                Container(
                    Div(
                        Img(src='/img/G.I.-Joe-Retro-Collection-Storm-Shadow-3.75-inch-Action-Figure-400x600.jpg', alt='Objetivo', cls='objetivo-img'),
                        Img(src='/img/reloj_avion.jpeg', alt='Objetivo', cls='objetivo-img'),
                        Img(src='/img/robot_reloj01.jpg', alt='Objetivo', cls='objetivo-img'),
                        cls='objetivo-imgs'
                    ),
                    Div(Li(
                        A('Feria ciruja | holocron sublimacion | $10000', href='/mostrar-descripcion'),
                        A('Borrar')
                       ),
                    Li(
                        A('Retro start | RGB | $11000', href='/mostrar-descripcion'),
                        A('Borrar')
                       ),
                    Li(
                        A('FAA | Gameshop | $15000', href='/mostrar-descripcion'),
                        A('Borrar')
                       ),
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
    contenido_body_aux=[Form(
                    Input(id='Feria', type='text', placeholder='Feria'),
                    Input(id='Local', type='text', placeholder='Local'),
                    Select(id='Moneda', placeholder='Moneda')(
                        Option('$', value='pesos', selected=True),
                        Option('u$d', value='dolares'),
                    ),
                    Input(id='Precio', type='number', placeholder='Precio'),
                    Input(id='Comentario', type='text', placeholder='Comentario'),
                    Button('Agregar', id='agregar'),
                    Button('Cancelar', id='cancelar', hx_get='/abrir-objetivo'),
                    action='/abrir-objetivo',
                    method='POST'
                )]
    
    contenidos.append(get_common_head(titulo='Bingo Bukku', contenido_body=contenido_body_aux))
    return Html(
        tuple(contenidos)
    )
