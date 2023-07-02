from fastapi import FastAPI
import os


# Obtener la ruta del directorio del archivo python actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Nombre del archivo json
file_name = "eventos.json"

# Combinar la ruta del directorio con el nombre del archivo JSON
file_path = os.path.join(dir_path, file_name)



app = FastAPI()


@app.get("/eventos")
def get_eventos(mes = None):

    import json
    import pandas as pd
    from datetime import datetime


    #url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

    # Leo el archivo json
    with open(file_path) as file:
        data = json.load(file)

    eventos = data['data']
    eventos_df = pd.DataFrame(eventos)
    atributos_se = eventos_df['attributes']
    atributos_df = pd.DataFrame(atributos_se.tolist())
    response_df = atributos_df[['id', 'name', 'date_start', 'date_end', 'ticket_value', 'suspendida']]

    if mes == None:
        response_json = response_df.to_json()
        return response_json

    else: 
        response_df_datetime = pd.to_datetime(response_df['date_start'])
        response_df['date_start'] = response_df_datetime
        # Con el metodo where busco todos los meses coincidentes con el parámetro recibido
        # Con dropna, quito los values NA que no coinciden con mi condición de búsqueda
        response_df_filtered = response_df.where(response_df['date_start'].dt.month == int(mes)).dropna()
        # Especificando el date_format logro que al transformar los tipos de datos DATE a JSON, estos no pierdan el formato de fecha
        response_json = response_df_filtered.to_json(date_format='iso')


        return response_json


@app.post("/eventos")
def post_eventos(id = str, name = str, suspendida = bool):
    
    import json
    from ocurrencias import Ocurrencia
    from attributes import Attributes

    #url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

    nuevos_atributos = Attributes(
        id= id,
        self="",
        name= name,
        dateFull={},
        date_start="2023-01-01",
        date_end="2023-01-02",
        text="",
        ticket="",
        ticket_value="",
        eventual_name="",
        eventual_direccion="",
        eventual_coords="",
        eventual_distrito="",
        suspendida= suspendida,
        status="",
        actividad="",
        regla="",
        regla_er=""
    )

    nuevos_atributos = dict(nuevos_atributos)

    nueva_ocurrencia = Ocurrencia(
        type="ocurrencias",
        id= id,
        attributes= nuevos_atributos,
        links={})
    

    # Leo el archivo json
    with open(file_path) as file:
        data = json.load(file)

    eventos = data['data']
    # Agrego el nuevo diccionario a la lista eventos
    eventos.append(dict(nueva_ocurrencia))
    # Piso el contenido de la lista eventos con la nueva ocurrencia
    data['data'] = eventos


    # Reescribir el json con los datos modificados
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    # Retornar una respuesta exitosa
    return {"message": "Evento añadido exitosamente"}

@app.put("/eventos")
def put_eventos(id = str, name = str):
    import json

    #url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

    with open(file_path) as file:
        data = json.load(file)

    eventos = data['data']
    # Actualizo el valor del nombre dentro del diccionario attributes
    for evento in eventos:
        if evento['id'] == str(id):
            print("Match entre ids")
            evento['attributes']['name'] = name

    
    # Reescribo el contenido de la variable data
    data['data'] = eventos
    print(data)
    

    # Reescribo el json con la actualización
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    # Retornar una respuesta exitosa
    return {"message": "Nombre de actualizado exitosamente"}




@app.delete("/eventos")
def delete_eventos(id = str):
    import json
    import pandas as pd

    #url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

    with open(file_path) as file:
        data = json.load(file)
    
    eventos = data['data']
    
    for evento in eventos:
        if str(evento['id']) == id:
            eventos.pop(evento)
            flag = True
            return {"message" : f"El evento con ID {evento['id']} ha sido eliminado exitosamente"}
            
    if not flag:
        return {"message" : f"El evento con ID {evento['id']} no existe en la plataforma"}
