


## Creación y publicación en PyPi de paquete con poetry
- [Creación y publicación en PyPi de paquete con poetry](#creación-y-publicación-en-pypi-de-paquete-con-poetry)
- [Instalación de poetry](#instalación-de-poetry)
- [Creación de paquete](#creación-de-paquete)
- [Construir tú paquete](#construir-tú-paquete)
- [Publicar tú paquete](#publicar-tú-paquete)
- [Referencias:](#referencias)



POETRY es el nuevo estándar para crear y gestionar el entorno virtual de tu proyecto Python. También es una herramienta de gestión de dependencias de Python que funciona de forma diferente a pip. Utiliza el nuevo estándar pyproject.toml decidido por la Autoridad de Embalaje de Python con PEP-518. Este archivo fusiona todos los archivos de configuración anteriores que eran necesarios, setup.py, requirements.txt, setup.cfg, MANIFEST.in y Pipfile, en un único archivo para gobernarlos a todos. Ok, basta de hablar del Señor del Anillo.

Te aconsejo que sigas la [documentación](https://python-poetry.org/docs/cli/) de poetry.

## Instalación de poetry
~~~
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
~~~

O empleando el comando
~~~
pip install poetry
~~~

Siéntase libre de mirar aquí para más [instrucciones](https://python-poetry.org/docs/). La actualización de `poetry` es fácil 

~~~
poetry update
~~~

## Creación de paquete
poetry tiene un buen comando que puede crear el árbol de su proyecto a la vez `poetry new <package_name>`.

~~~
/<package_name>
├── README.rst # Personalmente es mejor como Markdown, con la extensión .md
├── <package_name>
│   └── __init__.py
├── pyproject.toml
└── tests
    ├── __init__.py
    └── test_package_name.py
~~~

Deberá agregar cosas al archivo generado `pyproject.toml`, no dude en consultar la [documentación](https://python-poetry.org/docs/pyproject/) de poetry para ver todas las opciones.

~~~
[tool.poetry]
name = "vspoetry"
version = "0.0.0"
description = "Description of your package"
authors = ["JuanPerez <juanperez@gmail.com>"]
keywords = ["keyword", "another_keyword"]
readme = "README.md"
license = "MIT"
homepage = "https://github.com/JuanPerez/package_name"
repository = "https://github.com/JuanPerez/package_name"
include = [
    "LICENSE",
]

[tool.poetry.dependencies]
python = "^3.5"

[tool.poetry.dev-dependencies]

[tool.poetry.scripts]
cli_command_name = 'package_name:module_name:function'

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
~~~

El comienzo del archivo es bastante sencillo. Centrémonos en esas tres partes:

- [tool.poetry.dependencies]: aquí es donde puede enumerar todas las dependencias que su paquete necesita para funcionar. Es como el archivo antiguo requirements.txt . Puede hacerlo a mano y luego llamar al comando ``poetry install`` para instalarlos todos para el desarrollo de su paquete y propósitos de trabajo. Si usa ``poetry add <dependency_name>``(equivalente a pip install <dependency_name>), poetry lo agregará allí por usted.

- [tool.poetry.dev-dependencies]: Si necesita dependencias de desarrollo, ahí es donde van. Nuevamente, también puede instalarlos con ``poetry add <dependency_name> --dev`` (o -D) y poetry también lo colocará en el lugar correcto en su archivo pyproject.toml.

- [tool.poetry.scripts] : Este último bloque es muy importante si desea que su paquete tenga un script invocable desde la terminal.

~~~
script_name = '{package_name}:{function_name}'
~~~

Por cierto, si aún necesita tener un requirements.txt con todas las dependencias (si usa Heroku por ejemplo), puede tenerlo fácilmente con este comando:

~~~
poetry export -f requirements.txt > requirements.txt
~~~

## Construir tú paquete

Cuando su paquete esté listo, simplemente haga ``poetry build`` para crear los archivos del paquete

~~~
❯ poetry build
Building package_name (0.1.0)
 - Building sdist
 - Built package_name-0.1.0.tar.gz

 - Building wheel
 - Built package_name-0.1.0-py3-none-any.whl
~~~

Puede probar su paquete haciendo

~~~
pip install <path_to_package_name-0.1.0-py3-none-any.whl>
~~~

Si todo funciona, ¡felicidades! Ahora publíquelo en PyPi para que otros también puedan usar su gran paquete.

## Publicar tú paquete

Antes de publicar, primero debe crear una cuenta en [PyPi](https://pypi.org/account/register/). También puede registrar una cuenta en [TestPyPi](https://test.pypi.org/account/register/) si desea publicar en un repositorio de prueba antes de probar en el oficial.

Su paquete debe estar construido, así que primero ejecútelo ``poetry build`` si aún no lo ha hecho.

Luego, simplemente ejecute ``poetry publish`` y su paquete se publicará en PyPi:

~~~
❯ poetry publish

Publishing vspoetry (0.1.0) to PyPI
Username: Mattioo
Password:
 - Uploading vspoetry-0.1.0-py3-none-any.whl 100%
 - Uploading vspoetry-0.1.0.tar.gz 100%
~~~

Si necesita actualizar su paquete, simplemente incremente la versión en el archivo pyproject.toml y use ``poetry publish``(después de construir el nuevo paquete con ``poetry build``).

Una vez que haya hecho eso, puede instalar su paquete:

~~~
pip install <your_package>

poetry add <your_package> # pero seamos sinceros, ahora usas poetry, así que harías esto.
~~~

Felicidades por publicar su paquete en PyPi y experimentar la simplicidad de usar una herramienta como Poetry.

## Referencias:
- [Publish a package on PyPi using Poetry](https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/)
- [Create and Publish a Python Package with Poetry](https://johnfraney.ca/posts/2019/05/28/create-publish-python-package-poetry/)
- [How to package a Python](https://py-pkgs.org/03-how-to-package-a-python.html)

Forma tradicional:
- [Packaging to PyPi in Python](https://replit.com/talk/learn/How-to-create-python-packages-and-upload-to-pypi/35236)
- [Setuptools](https://docs.hektorprofe.net/python/distribucion/setuptools/)

Importación de paquetes
- [Using Objects from the Imported Module or Package](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)