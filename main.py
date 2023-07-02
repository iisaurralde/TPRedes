'''Defina cuáles serán las funciones del servidor API, qué funcionalidad cumple,
 ¿qué preguntas responde?, ¿qué datos del json permite cambiar?'''

# El servidor responde a un ciudadano o turista de la Ciudad de Rosario que requiere consultar los eventos disponibles en la ciudad
# Tambien responde a un administrador que requiere cargar/modificar/eliminar eventos

#### 1. El usuario tipo usuario podrá consultar mediante el Cliente todos los eventos, o los existentes en determinada fecha, rango.
#### 1.1. El Servidor deberá responder con el nombre del evento, fecha, dirección y el estado (suspendida o vigente)
#### 2. Un usuario tipo administrador podra leer/cargar/modificar/eliminar eventos.


from fastapi import FastAPI


app = FastAPI()



@app.get("/eventos")
def get_eventos(mes = None):

    import json
    import pandas as pd

    url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

    # Leo el archivo json
    with open(url) as file:
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
        response_df['date_start'] = pd.to_datetime(response_df['date_start'])
        response_df_filted = response_df[response_df['date_start'].dt.month == int(mes)]
        response_df_filted['date_start'] = str(response_df_filted['date_start'])
        response_json = response_df_filted.to_json()

        return response_json


@app.post("/eventos")
def post_eventos(id = str, name = str, suspendida = bool):
    
    import json
    from ocurrencias import Ocurrencia
    from attributes import Attributes

    url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

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
    with open(url) as file:
        data = json.load(file)

    eventos = data['data']
    # Agrego el nuevo diccionario a la lista eventos
    eventos.append(dict(nueva_ocurrencia))
    # Piso el contenido de la lista eventos con la nueva ocurrencia
    data['data'] = eventos


    # Reescribir el json con los datos modificados
    with open(url, 'w') as file:
        json.dump(data, file, indent=4)
    
    # Retornar una respuesta exitosa
    return {"message": "Evento añadido exitosamente"}

@app.put("/eventos")
def put_eventos(id = str, name = str):
    import json

    url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

    with open(url) as file:
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
    with open(url, 'w') as file:
        json.dump(data, file, indent=4)
    
    # Retornar una respuesta exitosa
    return {"message": "Nombre de actualizado exitosamente"}





@app.delete("/eventos")
def delete_eventos(id = str):
    import json
    import pandas as pd

    url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

    with open(url) as file:
        data = json.load(file)
    
    eventos = data['data']
    
    for evento in eventos:
        if str(evento['id']) == id:
            eventos.pop(evento)
            flag = True
            return {"message" : f"El evento con ID {evento['id']} ha sido eliminado exitosamente"}
            
    if not flag:
        return {"message" : f"El evento con ID {evento['id']} no existe en la plataforma"}

