from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return { "description" : "Hello Caruso - version 1"}