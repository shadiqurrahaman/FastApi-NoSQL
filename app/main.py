from fastapi import FastAPI
from . import(config,db,models)
from cassandra.cqlengine.management import sync_table

settings = config.get_settings()
product = models.Products
unique_product = models.UniqueProduct
session = None

app = FastAPI()

@app.on_event("startup")
def on_startup():
    global session
    session = db.get_session()
    sync_table(product)
    sync_table(unique_product)

@app.get('/')
def read_index():
    return "Hello Fast Api"

@app.get('/products')
def get_all_product():
    return {"results":list(product.objects().all())}