# API for users
# Run the server: uvicorn users:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Manually option (add each user)

@app.get("/usersjson") # http://127.0.0.1:8000/users
async def usersjson():
    return [{"name": "Esteban", "surname" : "Hernan", "website": "https://esteban.dev"},
            {"name": "Viviana", "surname" : "Escorcia", "website": "https://viviana.co"},
            {"name": "Andres", "surname" : "Perez", "website": "https://andres.com.br"}]

# User class

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    website: str

# Fake data base

users_list = [User(id=1, name="Esteban", surname="Hernandez", website="https://esteban.dev", age=28),
         User(id=2, name="Viviana", surname="Escorcia", website="https://viviana.co", age=30),
         User(id=3, name="Andres", surname="Perez", website="https://andres.com.br", age=36)] 

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "User not found"}

# GET
# GET http://127.0.0.1:8000/users

@app.get("/users") # http://127.0.0.1:8000/users
async def users():
    return users_list

# Path

@app.get("/user/{id}") # http://127.0.0.1:8000/user/2/Viviana
async def user(id: int):
    return search_user(id)
    
# Query

@app.get("/user/") # http://127.0.0.1:8000/user/?id=2&name=Viviana
async def user(id: int):
    return search_user(id)

# POST
# POST http://127.0.0.1:8000/user
# Content-Type: application/json

# {
#     "id": 4,
#     "name": "John",
#     "surname": "Doe",
#     "website": "john.doe.com",
#     "age": 30
# }

@app.post("/user", response_model=User, status_code=201)
async def user_add(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=405, detail="This user already exists")
    else:
        users_list.append(user)
        return user
    
# PUT
# PUT  http://127.0.0.1:8000/users
# Content-Type: application/json

# {
#     "id": 4,
#     "name": "John",
#     "surname": "Doe",
#     "website": "https://johndoe.com",
#     "age": 37
# }

@app.put("/users", response_model=User, status_code=200)
async def user_update(user: User):
    found_user = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found_user = True
    
    if not found_user:
        raise HTTPException(status_code=404, detail="This user doesnt exists, please create it")
    else:
        return user
    
# DELETE
# DELETE http://127.0.0.1:8000/user/4

@app.delete("/user/{id}", response_model=dict, status_code=200)
async def user_delete(id: int):
    found_user = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found_user = True

    if not found_user:
        raise HTTPException(status_code=404, detail="This user could not be deleted")
    else:
        return {"Success": "User deleted", "id": id}