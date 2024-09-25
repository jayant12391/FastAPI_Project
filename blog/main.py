from fastapi import FastAPI  
from . import models 
from .database import engine 
from typing import List 
from .routers import blog , user , authentication
from routers.authentication import app as authentication_app



app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)

app.include_router(blog.router)
app.include_router(user.router)

class Blog:
    def __init__(self):
        self.items = [] 

        blog = Blog()
        blog.items  # Ensure you're accessing the 'items' attribute correctly



print("Akash Thubrikar")





