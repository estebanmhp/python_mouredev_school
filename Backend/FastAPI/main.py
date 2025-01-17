# API Basics

from fastapi import FastAPI

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

