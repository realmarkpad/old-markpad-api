from fastapi import FastAPI
# from app.database import db

app = FastAPI()


@app.get("/{file_path:path}")
def root(file_path: str):
    return {
        "path": file_path,
        "content": "",
        "password": "",
        "child": [],
    }
