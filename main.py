from fasthtml.common import *

app, rt = fast_app(
                live=True,
                pico=False,
                static_path='statics'
            )

@rt('/')
def get():
    login = Html(
        Meta(charset='utf-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(rel='stylesheet', href='/styles/bingobukku.css', type='text/css'),
        Link(rel='stylesheet', href='/styles/login.css', type='text/css'),
        Link(rel='icon', href='/img/favicon.png', type='text/css'),
        Head(
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

    return login

@rt('/indice')
def index():
    return Html(
        Meta(charset='utf-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(rel='stylesheet', href='/styles/bingobukku.css', type='text/css'),
        Link(rel='stylesheet', href='/styles/indice.css', type='text/css'),
        Link(rel='icon', href='/img/favicon.png', type='text/css'),
        Head(
            Title('Bingo Bukku'),
            Body(
                Header('Usuario', cls='titulo'),
                Container(
                    A('Agregar objetivo', href='/agregar-objetivo'),
                    Div(
                        Li(
                            A('Objetivo 1', href='/abrir-objetivo')
                        ),
                    cls='objetivos'),
                ),
                Footer(Span('Copyright © 2025'))
            )
        )
    )

@rt('/agregar-objetivo')
def agregar_objetivo():
    return Html(
        Meta(charset='utf-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(rel='stylesheet', href='/styles/bingobukku.css', type='text/css'),
        Link(rel='stylesheet', href='/styles/objetivo.css', type='text/css'),
        Link(rel='icon', href='/img/favicon.png', type='text/css'),
        Head(
            Title('Agregar Objetivo'),
            Body(
                Form(
                    Input(id='Objetivo', type='text', placeholder='Objetivo'),
                    Button('Aceptar', id='aceptar'),
                    Button('Cancelar', id='cancelar', hx_get='/indice', hx_target='#contenido'),
                    action='/indice',
                    method='POST'
                )
            )
        )
    )

@rt('/abrir-objetivo') 
def abrir_objetivo():
    return Html(
        Meta(charset='utf-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(rel='stylesheet', href='/styles/bingobukku.css', type='text/css'),
        Link(rel='stylesheet', href='/styles/objetivo.css', type='text/css'),
        Link(rel='icon', href='/img/favicon.png', type='text/css'),
        Head(
            Title('Objetivo 1'),
            Body(
                Header(
                    'Objetivo 1',
                    A('Volver', href='/indice')
                    ),
                Container(
                    'Imagenes',
                    Li(
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
                    A('Agregar descripcion', href='/agregar-descripcion'),
                ),
                Footer('Copyright © 2025')
            )
        )
    )

@rt('/agregar-descripcion')
def agregar_descripcion():
    return Html(
        Meta(charset='utf-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(rel='stylesheet', href='/styles/bingobukku.css', type='text/css'),
        Link(rel='stylesheet', href='/styles/descripcion.css', type='text/css'),
        Link(rel='icon', href='/img/favicon.png', type='text/css'),
        Head(
            Title('Agregar Descripcion'),
            Body(
                Form(
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
                )
            )
        )
    )


serve()
