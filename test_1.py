import pandas as pd 
import json

url =r'/home/romanov/Documents/Project_G/books.json'

with open(url) as file:
    data = json.load(file)

print(data)



