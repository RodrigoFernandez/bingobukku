# Bingo Bukku (bingobukku)

Uso de:

* <https://www.fastht.ml/>
* <https://sqlmodel.tiangolo.com/>


## Para ejecutar el proyecto usar:

```
poetry run python main.py
```

## Pendientes

Puntos a ver:

* Agregar validaciones en los formularios de alta
* Ver cómo mostrar los mensajes al usuario (de error, alerta o exito)
* Si no hay imagen poner un link de alta (botón con un +, con tooltip de agregar imagen, y quizas con un texto de subtítulo indicando que va una imagen (?))
* Hacer lógica para subir imagen al servidor, ver cómo se hace esto. Actualizar el objetivo con la ruta en el servidor de la imagen subida.
* Mejorar el link de volver (de un objetivo al indice, poner un kunai (?))
* Mejorar estilos en los formularios
* Mejorar la estructura de una descripción (cambiar nombres de campos, reordenar campos en el formulario de ingreso)
* Hacer logica para mostrar todo el detalle (link mostrar-descripcion, que tenga un botón para eliminar, sería la lógica del punto de abajo)
* Hacer lógica para dar de baja una descripción (la X al final de cada descripción)
* Hacer lógica de login
* Ver como sería el tema de las sesiones en FastHTML
* En la pantalla de login agregar un link para el alta de un nuevo usuario
* Hacer página y lógica para el alta de usuarios
* Hacer lógica para mostrar info del usuario logueado
* Mejorar el header para que muestre: Bingo Bukku (en el centro) link_nombre_usuario (para ver sus datos) link_logout (para salir de la aplicación) [o algo asi, (?)] estos 2 links van alineados a la derecha
* En el indice, agregar link botón X a cada objetivo para poder eliminarlo
* Hacer lógica para la baja de objetivos
* Ver cómo funciona en un celular
* Agregar los media query necearios en los css
* Revisar todos los css para evitar los scroll innecesarios
* Revisar todos los css para que el footer siempre quede abajo de todo en todas las pantallas
* Ver como es el tema de async en FastHTML
* Ver si vale la pena agregar un filtro para ver como se hacen las consultas en SQLModel

---
---

## Consultas a chatgpt

### Subir archivo al servidor

¡Claro! Para subir una imagen en tu aplicación FastHTML, puedes seguir el siguiente ejemplo que utiliza el componente `UploadFile` de Starlette. Este ejemplo maneja la carga de una sola imagen, pero también puedes adaptarlo para múltiples imágenes si lo necesitas.

### 📁 Subir una imagen con FastHTML

```python
from fasthtml.common import *
from pathlib import Path

app, rt = fast_app()

upload_dir = Path("uploads")
upload_dir.mkdir(exist_ok=True)

@rt('/')
def get():
    return Titled("Subir Imagen",
        Article(
            Form(hx_post=upload, hx_target="#result")(
                Input(type="file", name="file", accept="image/*"),
                Button("Subir", type="submit", cls='secondary'),
            ),
            Div(id="result")
        )
    )

def FileCard(file):
    return Article(
        Header(H3(file.filename)),
        Ul(
            Li('Tamaño: ', file.size),
            Li('Tipo: ', file.content_type),
            Li('Encabezados: ', file.headers),
        )
    )

@rt('/upload')
async def upload(file: UploadFile):
    filebuffer = await file.read()
    (upload_dir / file.filename).write_bytes(filebuffer)
    return FileCard(file)

serve()
```

### 📝 Explicación del código

1. **Formulario de carga**: El formulario HTML se genera utilizando el componente `Form` de FastHTML. Se especifica `hx_post=upload` para enviar el formulario al endpoint `/upload` y `hx_target="#result"` para actualizar el contenido del `Div` con id `result` con la respuesta del servidor.

2. **Manejo de archivos**: En el endpoint `/upload`, se recibe el archivo cargado como un objeto `UploadFile`. Se lee el contenido del archivo y se guarda en el directorio `uploads` utilizando la biblioteca `pathlib`.

3. **Respuesta**: Después de guardar el archivo, se genera una tarjeta con la información del archivo (nombre, tamaño, tipo y encabezados) y se devuelve como respuesta. Esta tarjeta se inserta en el `Div` con id `result` en la página.

### 📂 Subir múltiples imágenes

Para permitir la carga de múltiples imágenes, puedes modificar el formulario y el endpoint de la siguiente manera:

```python
@rt('/')
def get():
    return Titled("Subir Imágenes",
        Article(
            Form(hx_post=upload_many, hx_target="#result")(
                Input(type="file", name="files", multiple=True, accept="image/*"),
                Button("Subir", type="submit", cls='secondary'),
            ),
            Div(id="result")
        )
    )

@rt('/upload')
async def upload(request: Request):
    form = await request.form()
    files = form.getlist("files")
    cards = []
    for file in files:
        filebuffer = await file.read()
        (upload_dir / file.filename).write_bytes(filebuffer)
        cards.append(FileCard(file))
    return cards
```

En este caso:

* El formulario permite seleccionar múltiples archivos mediante `multiple=True`.
* En el endpoint `/upload`, se obtiene la lista de archivos utilizando `form.getlist("files")`.
* Se procesan y guardan cada uno de los archivos, y se genera una tarjeta para cada uno.

### ⚠️ Consideraciones de seguridad

Al permitir la carga de archivos, es importante tener en cuenta las siguientes consideraciones de seguridad:

* **Validar el tipo de archivo**: Asegúrate de que los archivos cargados sean del tipo esperado (por ejemplo, imágenes). Puedes verificar el tipo MIME del archivo utilizando `file.content_type`.

* **Limitar el tamaño del archivo**: Establece un tamaño máximo para los archivos cargados para evitar el consumo excesivo de recursos. Puedes verificar el tamaño del archivo utilizando `file.size`.

* **Evitar la sobrescritura de archivos existentes**: Al guardar los archivos, asegúrate de que no sobrescriban archivos existentes con el mismo nombre. Puedes generar nombres únicos para los archivos utilizando, por ejemplo, un identificador único o un timestamp.

* **Almacenar los archivos en un directorio seguro**: Asegúrate de que el directorio donde se almacenan los archivos cargados no sea accesible públicamente para evitar la ejecución de archivos maliciosos.

Si necesitas ayuda para implementar estas medidas de seguridad o tienes alguna otra pregunta, no dudes en consultarme. ¡Estoy aquí para ayudarte!

