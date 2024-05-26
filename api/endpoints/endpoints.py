from fastapi import Header, Depends
from main import app

@app.get("/")
async def root():

    return {"message": "Bem Vindo a API EMBRAPA"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Olá {name}"}