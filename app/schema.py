from pydantic import BaseModel,ValidationError 

# this is for create validation on data base

class ProductSchema(BaseModel):
    name: str
    title:str
    age:str



