#!/bin/bash

echo "Trying to install dependencies..."

# Verificar si Python está instalado
if ! command -v python3 &>/dev/null; then
    echo "Python no está instalado. Instalando..."
    # Ejecutar el comando de instalación de Python (depende del sistema operativo)
    # Por ejemplo, en Ubuntu puedes usar: sudo apt-get install python3
    # Asegúrate de ajustar el comando según tu sistema operativo
    exit 1
else
    echo "Python ya está instalado."
fi

# Verificar si pip está instalado
if ! command -v pip3 &>/dev/null; then
    echo "pip no está instalado. Instalando..."
    # Ejecutar el comando de instalación de pip (depende del sistema operativo)
    # Por ejemplo, en Ubuntu puedes usar: sudo apt-get install python3-pip
    # Asegúrate de ajustar el comando según tu sistema operativo
    exit 1
else
    echo "pip ya está instalado."
fi

# Verificar y instalar dependencias
dependencies=( "pandas", "request", "json")

for dependency in "${dependencies[@]}"
do
    # Verificar si la dependencia está instalada
    if ! python3 -c "import $dependency" &>/dev/null; then
        echo "La dependencia $dependency no está instalada. Instalando..."
        # Ejecutar el comando de instalación de la dependencia
        pip3 install $dependency
    else
        echo "La dependencia $dependency ya está instalada."
    fi
done

echo "Dependencies installation completed."