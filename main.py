from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data':{'name':'jayant'}}

@app.get('/about')
def about():
    return {'data':'this is about page'}