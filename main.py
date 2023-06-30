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
    #request_df = pd.read_json(response_json)

    if mes == None:
        response_json = response_df.to_json()
        return response_json

    else: 
        response_df['date_start'] = pd.to_datetime(response_df['date_start'])
        response_df_filted = response_df[response_df['date_start'].dt.month == int(mes)]
        response_df_filted['date_start'] = str(response_df_filted['date_start'])
        response_json = response_df_filted.to_json()

        return response_json


