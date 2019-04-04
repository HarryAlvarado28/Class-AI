##!/bin/bash

#Instala el entorno virtual de Python (si no lo tienes):
`pip install virtualenv`

# Prepara el entorno virtual:
`virtualenv -p python3 env`

# Activa el entorno:
`source env/bin/activate`

# Instala GYM-Retro:
`pip3 install gym-retro`

# Importa del roms el archivo de Sonic:
`python3 -m retro.import roms`
