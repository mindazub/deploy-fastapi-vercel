from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}
    
@app.get("/third")
def home():
    return {"message": "Hello third"}

@app.get("/frogs")
def home():
    return {"message": "Hello frogs"}


    