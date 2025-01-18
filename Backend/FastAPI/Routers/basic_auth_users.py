from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel): # Public
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User): # Private
    password: str

users_db = {
    "estebanhp22": {
        "username": "estebanhp22",
        "full_name": "Esteban Hernandez",
        "email": "estebandev@example.com",
        "disabled": False,
        "password": "123456"
    },
    "wiwisdesign": {
        "username": "wiwisdesign",
        "full_name": "Viviana Escorcia",
        "email": "wiwisdesing@example.com",
        "disabled": True,
        "password": "987654"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Unauthorized:(incorrect details)", 
            headers={"WWW-Authenticate": "Bearer"})
    
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Forbidden:(user is disabled)")
    
    return user

# POST  http://127.0.0.1:8000/login
# Content-Type: application/x-www-form-urlencoded

# username=estebanhp22&password=123456    

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found(invalid user)")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized:(incorrect password)")
    
    return {"access_token": user.username, "token_type": "bearer"}

# GET   http://127.0.0.1:8000/users/me
# Authorization: Bearer estebanhp22

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user