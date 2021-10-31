from pydantic import BaseModel,ValidationError,root_validator
from typing import Optional,Any
import datetime

# this is for create validation on data base

class ProductSchema(BaseModel):
    name: str
    title:str
    age:str

class UniqueProductschemaList(BaseModel):
    name:Optional[str]
    title:str

class UniqueProductschema(BaseModel):
    name:Optional[str]
    title:str
    created:Optional[Any]=None

    @root_validator(pre=True)
    def create_time_from_uuid(cls,values):
        values['created'] = uuid_time_to_python_datetime(values['uuid'].time)
        return values



def uuid_time_to_python_datetime(time:int):

    return datetime.datetime(1582,10,15)+datetime.timedelta(microseconds=time//10)

