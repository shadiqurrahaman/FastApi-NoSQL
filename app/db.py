
import os
import pathlib

from dotenv import load_dotenv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from cassandra.cqlengine import connection



BASE_DIR = pathlib.Path(__file__).parent
CLUSTER_BUNDLE = str(BASE_DIR / "ignored" / 'connect.zip')
load_dotenv()


ASTRADB_CLINT_ID = os.environ.get('ASTRADB_CLINT_ID')
ASTRADB_CLINT_SECRET = os.environ.get('ASTRADB_CLINT_SECRET')
ASTRADB_TOKEN = os.environ.get('ASTRADB_TOKEN')


def get_cluster():
    cloud_config= {
        'secure_connect_bundle': CLUSTER_BUNDLE
    }
    auth_provider = PlainTextAuthProvider(ASTRADB_CLINT_ID, ASTRADB_CLINT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster

def get_session():
    cluster = get_cluster()
    session = cluster.connect()
    connection.register_connection(str(session), session=session,default=True)
    connection.set_default_connection(str(session))
    return session


# session = get_session()
# row = session.execute("select release_version from system.local").one()
# if row:
#     print(row[0])
# else:
#     print("An error occurred.")