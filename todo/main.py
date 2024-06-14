from fastapi import FastAPI 
import uvicorn
from jose import jwt


app = FastAPI()

SECRET= "I am secret key"

ALGORITHEM= 'HS256'

def jwt_token(subject:str):
    token = jwt.encode({'data': subject}, SECRET, algorithm=ALGORITHEM)
    return token

def decode_token(token):
    token=jwt.decode(token, SECRET, algorithms=[ALGORITHEM])
    return token


@app.get("/token/")
def create_token(name:str):
    token = jwt_token(name)
    return token

@app.get("/decodetoken/")
def create_decode_token(token:str):
    token = decode_token(token)
    return token

# dependancy injection: Means the function that depends on other function





def start():
    uvicorn.run("todo.main:app", host="127.0.0.1", port= 8080, reload=True)


