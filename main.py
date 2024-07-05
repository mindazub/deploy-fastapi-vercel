from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Taigi penkto uzteks. Pakanka tik git push -u origin main."}



    