# API for users with Mongo DB

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client # Connect to Mongo DB
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"Error": "Not found"}}) 

def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"Error": "User not found"}

# GET

@router.get("/", response_model=list[User]) 
async def users_get():
    return users_schema(db_client.users.find())

# Path

@router.get("/{id}") 
async def user(id: str):
    return search_user("_id", ObjectId(id))
    
# Query

@router.get("/") 
async def user(id: str):
    return search_user("_id", ObjectId(id))

# POST

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user_add(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status.HTTP_405_METHOD_NOT_ALLOWED, detail="This user already exists")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id
    
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)
    
# PUT

@router.put("/", response_model=User, status_code=status.HTTP_200_OK)
async def user_update(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    try:
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="This user doesnt exists, please create it")

    return search_user("_id", ObjectId(user.id))
    
    
# DELETE

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user_delete(id: str):

    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="This user could not be deleted")

