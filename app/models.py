
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


data = {
    'asin':"dsjhfskjdhf1",
    'title': "Mark 1"
}

class Products(Model):
    __keyspace__ = 'fast_api_app'
    asin  = columns.Text(primary_key=True)
    title = columns.Text()


class UniqueProduct(Model):
    __keyspace__ = 'fast_api_app'
    uuid = columns.UUID(primary_key=True)
    asin  = columns.Text(index=True)
    title = columns.Text()

