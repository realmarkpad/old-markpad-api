from fastapi import FastAPI, HTTPException
from starlette.responses import Response
from app.database import db

app = FastAPI()


@app.get("/{file_path:path}", status_code=200)
async def get_document(file_path: str, response: Response):
    requested_doc = await db.document.find_one({"path": file_path})
    if requested_doc is None:
        raise HTTPException(
            status_code=404,
            detail="The document {path} don't exist!".format(path=file_path)
        )
    return requested_doc


@app.post("/{file_path:path}", status_code=201)
async def insert_document(file_path: str):
    default_new_doc = {
        "path": file_path,
        "content": "",
        "password": "",
        "child": []
    }
    result = await db.document.insert_one(default_new_doc)
    return {"_id": str(result.inserted_id)}
