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
        print("\n -- Ingrese (3) para salir... ")
        usuario = input()

    if usuario == "1":
            while True:
                print("\n\n:: Bienvenido al menu de Usuarios ::")
                print("\n\n-- Opciones:\n1)Ver todos los eventos del año\n2)Ver los eventos de un mes en particular\n3)Presione (3) para salir al menu anterior")
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

                elif opcion == "2":
                    print("\n\nIngrese un número del 1 al 12, referente al número de mes que desea consultar...")
                    mes = input()
                    while int(mes) not in list(range(1,13)):
                        print("\nNro de mes incorrecto!")
                        print("\nIngrese un número del 1 al 12, referente al número de mes que desea consultar...")
                        mes = input()

                    uri = url + "/eventos?mes=" + mes
                    response = rq.get(uri)
                    response_json = json.loads(response.text)
                    response_df = pd.read_json(response_json)
                    if not response_df.empty:    
                        print(f"\n -> Estos son todos los eventos del mes seleccionado registrados en nuestra plataforma: \n\n{response_df[['name', 'date_start', 'ticket_value']]}")
                    else:
                        print("\nNo existen eventos registrados en el mes seleccionado")

                else:
                    break





    if usuario == "2":
        while True:
                print("\n\n:: Bienvenido al menu de Administradores ::")
                print("""\n\n-- Opciones:
                                    \n1) Ver todos los eventos del año
                                    \n2) Ver los eventos de un mes en particular
                                    \n3) Agregar un evento
                                    \n4) Actualizar un evento
                                    \n5) Eliminar un evento  
                                    \n6) Presione (6) para salir al menu anterior""")
                
                opcion = input()
                while int(opcion) not in list(range(1,7)):
                    print("\n\n¡Opción incorrecta! Por favor vuelva a ingresar una opción válida...")
                    print("""\n\n-- Opciones:
                                    \n1) Ver todos los eventos del año
                                    \n2) Ver los eventos de un mes en particular
                                    \n3) Agregar un evento
                                    \n4) Actualizar un evento
                                    \n5) Eliminar un evento  
                                    \n6) Presione (6) para salir al menu anterior\n\n""")
                    opcion = input()


                if opcion == "1":
                    uri = url + r"/eventos"
                    response = rq.get(uri)
                    response_json = json.loads(response.text)
                    response_df = pd.read_json(response_json)
                    
                    print(f"\n -> Estos son todos los eventos del año registrados en nuestra plataforma: \n\n{response_df[['name', 'date_start', 'ticket_value']]}")

                elif opcion == "2":
                    print("\n\nIngrese un número del 1 al 12, referente al número de mes que desea consultar...")
                    mes = input()
                    while int(mes) not in list(range(1,13)):
                        print("\nNro de mes incorrecto!")
                        print("\nIngrese un número del 1 al 12, referente al número de mes que desea consultar...")
                        mes = input()

                    uri = url + "/eventos?mes=" + mes
                    response = rq.get(uri)
                    response_json = json.loads(response.text)
                    response_df = pd.read_json(response_json)
                    if not response_df.empty:    
                        print(f"\n -> Estos son todos los eventos del mes seleccionado registrados en nuestra plataforma: \n\n{response_df[['name', 'date_start', 'ticket_value']]}")
                    else:
                        print("\nNo existen eventos registrados en el mes seleccionado")
                
                elif opcion == "3":
                    print("\n\nIngrese el ID del nuevo evento")
                    id = input()
                    print("\nIngrese el nombre del nuevo evento")
                    nombre = input()
                    uri = url + f"/eventos?id={id}&name={nombre}&suspendida=false"
                    response = rq.post(uri)
                    print(f"\n{response.text}")


                else:
                    break    
            
        
    
    if usuario == "3":
        print("Gracias por usar nuestra plataforma de eventos!! Hasta pronto...")
        break

