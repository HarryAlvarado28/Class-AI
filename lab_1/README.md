# Laboratorio 1 :cyclone: :metal:

Para ver correr este programa (lab1) debes ejecutar estos comandos:

Debes de tener Python 3.5+ instalado. :zap:

## Configuración del entorno

Seguir las siguientes instrucciones:

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

**Si Sonic se mueve, entonces ya funciona.**

## Instrucciones Originales

### Procedimiento de instalación:

- 1. Creen una carpeta llamada lab_1 y dentro de ella ejecutar:
```shell
virtualenv -p python3 env

source env/bin/activate

pip3 install gym-retro
```
- 2. Creen una carpeta llamada roms dentro de lab_1 y colocar el archivo md de sonic. Ejecutar:
```shell
python3 -m retro.import roms
```

- 3. Colocar el archivo controlador dentro de la carpeta lab_1, y ejecutar:
```shell
python sonic.py
```
**Si sonic se mueve, entonces ya funciona.**
