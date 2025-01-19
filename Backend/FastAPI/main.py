# API Basics

from fastapi import FastAPI
from Routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Run the server: uvicorn file_name:instance_of_fastAPI() -> uvicorn main:app --reload
# Stop the server: Ctrl + C

# Documentation with Swagger: http://12.0.0.1:8000/docs
# Documentation with ReDocly: http://12.0.0.1:8000/redoc

@app.get("/") # http://127.0.0.1:8000/
async def root():
    return "Hello FastAPI!"

@app.get("/url") # http://127.0.0.1:8000/url
async def url_course():
    return {"url_course": "https://mouredev.com/python"}

# ROUTERS

app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

# STATICS
# Example -> http://127.0.0.1:8000/statics/Images/Python-01.jpg

app.mount("/statics", StaticFiles(directory="Statics"), name="static")
