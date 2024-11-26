#!/usr/env/python3

import os

# Crear las carpetas directamente
os.makedirs('nmap', exist_ok=True)
os.makedirs('content', exist_ok=True)
os.makedirs('exploits', exist_ok=True)
os.makedirs('scripts', exist_ok=True)

print("Carpetas creadas exitosamente.")