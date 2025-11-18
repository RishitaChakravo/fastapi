from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post('/blog')
def create(request: schemas.Blog):
    return {'data' : {
        'title' : request.title,
        'body' : request.body
    }}