from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : {
        'name' : "Rishita",
        'age' : 19,
        'roll_no' : 64
    }}

@app.get('/about')
def about():
    return  {'data' : "About Page"}