import uuid
from .models import Products,UniqueProduct
from .db import get_session
from cassandra.cqlengine.management import sync_table

session = get_session()
sync_table(Products)
sync_table(UniqueProduct)


def create_entry(data:dict):
    return Products.create(**data)

def create_unique_entry(data:dict):
    data['uuid'] = uuid.uuid1()
    return UniqueProduct.create(**data)

def add_unique_entry(data:dict):
    product = create_entry(data)
    unique_product= create_unique_entry(data)
    return product,unique_product    

