from fastapi import FastAPI
from . import(config)

settings = config.get_settings()

app = FastAPI()

@app.get('/')
def read_index():
    return "Hello Fast Api"