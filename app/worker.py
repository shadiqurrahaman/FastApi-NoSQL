from celery import Celery
from . import config
from celery.signals import (beat_init,worker_process_init)
from . import (config,db,models)
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

celery_app = Celery(__name__)

settings = config.get_settings()
celery_app.conf.broker_url = settings.redis_url
celery_app.conf.result_backend = settings.redis_url
Product = models.UniqueProduct

def celery_on_startup(*args,**kwargs):
    print("hello world")
    cluster = db.get_cluster()
    session = cluster.connect()
    connection.register_connection(str(session), session=session,default=True)
    connection.set_default_connection(str(session))
    sync_table(Product)

beat_init.connect(celery_on_startup)
worker_process_init.connect(celery_on_startup)

@celery_app.task
def random_task(name):
    print(f"who are you {name}")
    
@celery_app.task
def view_all_product():
    print(list(Product.objects().all()))