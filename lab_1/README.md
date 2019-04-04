# Laboratorio 1 :cyclone: :metal:

Para ver correr este programa (lab1) debes ejecutar estos comandos:

Debes de tener Python 3.5+ instalado. :zap:

## Configuración del entorno

```shell
pip3 install virtualenv  #Instala el entorno virtual de Python (si no lo tienes)

virtualenv -p python3 env  #Prepara el entorno virtual

source env/bin/activate   #Activa el entorno

pip3 install gym-retro    #Instala GYM-Retro

python3 -m retro.import roms    #Importa del roms el archivo de Sonic
```

Ya puedes ejecutar Sonic:
```shell
python sonic.py   #Ejecutando Sonic
```

## Recuerda

Recuerda que si terminas la sesion de la terminal donde ejecutastes sonyc, el entorno no habras desactivado, para esto debes de ejecutar nuevamente:

```shell
source env/bin/activate
```

y luego ejecutas Sonic:

```shell
python sonic.py
```
