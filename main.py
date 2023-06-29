from fastapi import FastAPI


app = FastAPI()


@app.get("/libros")

def get_json():
    import json

    url =r'/home/romanov/Documents/Project_G/books.json'

    with open(url) as file:
        data = json.load(file)


    return data

@app.get("/autores")

def get_autores():
    import json
    url =r'/home/romanov/Documents/Project_G/books.json'

    with open(url) as file:
        data = json.load(file)

    data
