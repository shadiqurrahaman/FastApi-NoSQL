from pydantic import BaseSettings,Field
from functools import lru_cache


class settings(BaseSettings):
    db_clint_id:str = Field(...,env='ASTRADB_CLINT_ID')
    db_clint_secret:str = Field(...,env='ASTRADB_CLINT_SECRET')
    redis_url:str = Field(...,env='REDIS_URL')

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return settings()