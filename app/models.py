
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


data = {
    'name':"name1",
    'title': "Mark 1",
    'age':"20"
}

class Products(Model):
    __keyspace__ = 'fast_api_app'
    name  = columns.Text(primary_key=True)
    title = columns.Text()
    age = columns.Text()


class UniqueProduct(Model):
    __keyspace__ = 'fast_api_app'
    uuid = columns.UUID(primary_key=True)
    name  = columns.Text(index=True)
    title = columns.Text()

