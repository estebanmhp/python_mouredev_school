from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
TOKEN_DURATION = 1
SECRET = "1a5c67ad8c2935f95269786d851bee514b9c9a65285ab9331fe4b8c1de2dc89c"

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl = "login")
crypt = CryptContext(schemes = ["bcrypt"])

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
        "password": "$2a$12$7Pyyfmv4E.BNf8t7xG41MuphJa0BpmFIaPakQyUh1MqJsw5nyX7US"
    },
    "wiwisdesign": {
        "username": "wiwisdesign",
        "full_name": "Viviana Escorcia",
        "email": "wiwisdesing@example.com",
        "disabled": True,
        "password": "$2a$12$saWgWqcgcgLLvBwJnjc0De5eMiPnC/NyHGZaGMxO7.jIy5.WyO7nG"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized:(incorrect details)",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    return search_user(username)
    
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Forbidden:(user is disabled)")
    
    return user

@app.post("/login/jwt")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found(invalid user)")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized:(incorrect password)")
    
    access_token = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_DURATION),
    }
    
    return {"access_token": jwt.encode(access_token, SECRET, algorithm = ALGORITHM), "token_type": "bearer"}

@app.get("/users/me/jwt")
async def me(user: User = Depends(current_user)):
    return user

