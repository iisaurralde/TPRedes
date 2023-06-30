import requests as rq
import json
import pandas as pd

ip = "127.0.0.1"
port = "8000"
url = ip + ":" + port

while True:

    print("::: Bienvenido a la app de eventos de la Municipalidad de Rosario :::")
    print("\n\n -- Ingrese (1) para operar como Usuario ")
    print("\n -- Ingrese (2) para operar como Administrador ")
    print("\n -- Ingrese (3) para salir... ")
    usuario = input()

    while usuario != "1" and usuario != "2" and usuario != "3":
        print("\n\n¡Opción incorrecta! Por favor vuelva a ingresar una opción válida...")
        print("\n\n -- Ingrese (1) para operar como Usuario ")
        print("\n -- Ingrese (2) para operar como Administrador ")
        usuario = input()

    if usuario == "1":
        print("Bienvenido al menu de Usuarios")
        print("\n\n-- Opciones:\n1)Ver todos los eventos del año\n2)Ver los eventos de un mes en particular\n3)Presione (3) para salir")
        opcion = input()
        while opcion != "1" and opcion != "2" and opcion != "3":
            print("\n\n¡Opción incorrecta! Por favor vuelva a ingresar una opción válida...")
            print("\n\n-- Opciones:\n1)Ver todos los eventos del año\n2)Ver los eventos de un mes en particular\n3)Presione (3) para salir")
            opcion = input()    
        
        print("Hola Usuario! Con esta aplicación usted podrá consultar todos los eventos que nuestra Muni tiene registrados para el año corriente")
        print("\n\n-- Ingrese (1) si desea consultar por todos los eventos")
        print("\n-- Ingrese (2) si desea consultar por los eventos de un mes en particular")
        print("\n-- Ingrese (3) si desea regresar al menu anterior")
        seleccion = input()
        while seleccion != "1" and seleccion != "2" and seleccion != "3":
            print("\n\n¡Opción incorrecta! Por favor vuelva a ingresar una opción válida...")
            print("\n\n-- Ingrese (1) si desea consultar por todos los eventos")
            print("\n-- Ingrese (2) si desea consultar por los eventos de un mes en particular")
            print("\n-- Ingrese (3) si desea regresar al menu anterior")
            seleccion = input()
        
    if usuario == "2":
        print("Programa en construcción...")
    
    if usuario == "3":
        print("Gracias por usar nuestra app de eventos!! Hasta pronto...")
        break
