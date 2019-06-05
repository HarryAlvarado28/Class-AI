# Laboratorio 1 :cyclone: :metal:

## Sonic corriendo

_**IMPORTANTE Seguir los pasos del [README Principal](https://github.com/HarryAlvarado28/Class-AI).**_

Si ya tienes el entorno activo, Ya puedes ejecutar Sonic

```console
python3 sonic.py                # Ejecutando Sonic
```

De lo contrario activa el entorno y ejecuta a Sonic

```shell
source env-classai/bin/activate # Activa el entorno

python3 sonic.py                # Ejecutando Sonic
```

**Si Sonic se mueve, entonces ya funciona.**

_**No es necesario si has siguido los pasos del [README Principal](https://github.com/HarryAlvarado28/Class-AI).**_

**Instrucciones Originales**

Procedimiento de instalación:

1. Creen una carpeta llamada lab_1 y dentro de ella ejecutar:
```shell
virtualenv -p python3 env

source env/bin/activate

pip3 install gym-retro
```
2. Creen una carpeta llamada roms dentro de lab_1 y colocar el archivo md de sonic. Ejecutar:
```shell
python3 -m retro.import roms
```

3. Colocar el archivo controlador dentro de la carpeta lab_1, y ejecutar:
```console
python3 sonic.py
```
**Si sonic se mueve, entonces ya funciona.**
