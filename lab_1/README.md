# sony-computing-machine :collision:

# Laboratorio 1 :metal:

Para ver correr este programa (lab1) debes ejecutar estos comandos:

Debes de tener Python 3.5+ instalado. :zap:

Instala el entorno virtual de Python (si no lo tienes):

`pip install virtualenv`

Prepara el entorno virtual:

`virtualenv -p python3 env`

Activa el entorno:

`source env/bin/activate`

Instala GYM-Retro:

`pip3 install gym-retro`

Importa del roms el archivo de Sonic:

`python3 -m retro.import roms`

Ya puedes ejecutar Sonic:

`python sonic.py`

### Más Rápido

Sección de plus, se a creado un script con toda la instalación del los pasos anteriores *skip_lol.sh*::

`source skip_lol.sh`

y luego ejecutar Sonic:

`python sonic.py`

## Curioso

Recuerda que si terminas la sesion de la terminal donde ejecutastes sonyc, el entorno no habras desactivado, para esto debes de ejecutar nuevamente:

`source env/bin/activate`

y luego ejecutas Sonic:

`python sonic.py`
