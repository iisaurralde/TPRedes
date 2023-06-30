
import json
import pandas as pd

url ='C:\\Users\\Nacho\\Documents\\TUIA\\Redes\\TPRedes\\eventos.json'

with open(url) as file:
    data = json.load(file)


eventos = data['data']
eventos_df = pd.DataFrame(eventos)
atributos_se = eventos_df['attributes']
atributos_df = pd.DataFrame(atributos_se.tolist())
response_df = atributos_df[['id', 'name', 'date_start', 'date_end', 'ticket_value', 'suspendida']]
response_json = response_df.to_json()
request_df = pd.read_json(response_json)


mes = "9"
response_df['date_start'] = pd.to_datetime(response_df['date_start'])
response_df_filted = response_df[response_df['date_start'].dt.month == int(mes)]

print(response_df_filted)
