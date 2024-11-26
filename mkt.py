#!/usr/env/python3

import os

# Lista de carpetas que deseas crear
carpetas = ['nmap', 'content', 'exploits', 'scripts']

# Crear cada carpeta
for carpeta in carpetas:
    try:
        # Comprobar si la carpeta ya existe, si no, crearla
        if not os.path.exists(carpeta):
            os.mkdir(carpeta)
            print(f'Carpeta {carpeta} creada exitosamente.')
        else:
            print(f'La carpeta {carpeta} ya existe.')
    except Exception as e:
        print(f'Error al crear la carpeta {carpeta}: {e}')
