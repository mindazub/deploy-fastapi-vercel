from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def about(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request, "name": "Blog ME"})

@app.get("/blog")
async def about(request: Request):
    return templates.TemplateResponse("blog.html",
                                      {"request": request, "name": "Blog ME"})

    