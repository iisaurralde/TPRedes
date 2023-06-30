
## Este script lo voy usando para pruebas de manipulación en los datos 

import json
import pandas as pd
import requests as rq

# url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

# with open(url) as file:
#     data = json.load(file)


# eventos = data['data']
# eventos_df = pd.DataFrame(eventos)
# atributos_se = eventos_df['attributes']
# atributos_df = pd.DataFrame(atributos_se.tolist())
# response_df = atributos_df[['id', 'name', 'date_start', 'date_end', 'ticket_value', 'suspendida']]
# response_json = response_df.to_json()
# request_df = pd.read_json(response_json)


# mes = "9"
# response_df['date_start'] = pd.to_datetime(response_df['date_start'])
# response_df_filted = response_df[response_df['date_start'].dt.month == int(mes)]

# # print(response_df_filted)
# ip = "127.0.0.1"
# port = "8000"
# url = r"http://127.0.0.1:8000/eventos"

# response = rq.get(url)
# #response_json = json.load(response.text)
# # response_df = pd.read_json(response_json.text)
# response_json = json.loads(response.text)
# response_df = pd.read_json(response_json)
# print(response_df[['name', 'date_start', 'ticket_value']])


print(list(range(1,12)))