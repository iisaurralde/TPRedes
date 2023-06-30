import requests as rq
import json
import pandas as pd

ip = r"http://127.0.0.1"
port = "8000"
url = ip + ":" + port

while True:

    print("\n\n::: Bienvenido a la app de eventos de la Municipalidad de Rosario :::")
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
        
        
        if opcion == "1":
            uri = url + r"/eventos"
            response = rq.get(uri)
            response_json = json.loads(response.text)
            response_df = pd.read_json(response_json)
            
            print(f"\n -> Estos son todos los eventos del año registrados en nuestra plataforma: \n\n{response_df[['name', 'date_start', 'ticket_value']]}")
        
    if usuario == "2":
        print("Programa en construcción...")
    
    if usuario == "3":
        print("Gracias por usar nuestra app de eventos!! Hasta pronto...")
        break
