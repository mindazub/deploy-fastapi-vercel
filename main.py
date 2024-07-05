from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}
    
@app.get("/frogs")
def home():
    return {"message": "Hello Frogs"}
    