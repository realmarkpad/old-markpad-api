from fastapi import FastAPI
# from app.database import db

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}
