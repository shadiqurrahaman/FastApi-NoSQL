from fastapi import FastAPI
from . import(config,db,models,schema,crud)
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
    return list(product.objects().all())

@app.get('/unique_product')
def get_all_unique_product():
    # data = dict(unique_product.objects().first())
    allunique = list(unique_product.objects().all())
    filteredData = [schema.UniqueProductschema(**x)for x in allunique]
    # data['events'] = filteredData
    return filteredData

@app.get('/unique_product/{name}')
def get_all_unique_product(name:str):
    # data = dict(unique_product.objects().first())
    allunique = list(unique_product.objects().filter(name=name))
    # filteredData = [schema.UniqueProductschema(**x)for x in allunique]
    # # data['events'] = filteredData
    return allunique



@app.post('/insert_unique_product')
def add_unique_product(data: schema.UniqueProductschemaList):
    uproduct = crud.create_unique_entry(data.dict())
    return uproduct
