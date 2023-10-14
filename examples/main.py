import os
from fastapi import FastAPI
from redis import Redis

app = FastAPI()

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PASS = os.environ.get('REDIS_PASS')
redis = Redis(host=REDIS_HOST, port=6379, password=REDIS_PASS)

@app.get('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return {"message": f"Webpage viewed {counter} time(s)"}