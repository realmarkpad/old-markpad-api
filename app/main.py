from fastapi import FastAPI, HTTPException
from starlette.responses import Response

from app.database import db

from typing import List
from pydantic import BaseModel


class Document(BaseModel):
    _id: str = None
    path: str
    content: str = ""
    child:  List[str] = []


app = FastAPI()


@app.get("/document/{file_path:path}", status_code=200)
async def get_document(file_path: str, response: Response):
    requested_doc = await db.document.find_one({"path": file_path})
    if requested_doc is None:
        raise HTTPException(
            status_code=404,
            detail="The document {path} don't exist!".format(path=file_path)
        )
    requested_doc['_id'] = str(requested_doc['_id'])
    return requested_doc


@app.post("/document/", status_code=201)
async def insert_document(doc: Document):
    alredy_on_db = await db.document.find_one({"path": doc.path}) is not None
    if alredy_on_db:
        raise HTTPException(
            status_code=409,
            detail="The document {path} alredy exist!".format(path=doc.path)
        )

    list_path = doc.path.split("/")
    if len(list_path) > 1:
        new_child = list_path.pop()
        parent_path = "/".join(list_path)

        parent = await db.document.find_one({"path": parent_path})
        if parent is None:
            raise HTTPException(
                status_code=400,
                detail="The document {path} is orphan!".format(path=doc.path)
            )

        parent["child"].append(new_child)
        await db.document.update_one(
            {"path": parent_path},
            {"$set": {"child": parent["child"]}}
        )

    default_new_doc = {
        "path": doc.path,
        "content": "",
        "child": []
    }
    result = await db.document.insert_one(default_new_doc)
    return {"_id": str(result.inserted_id)}


@app.put("/document/", status_code=200)
async def update_document(doc: Document):
    result = await db.document.update_one(
        {"path": doc.path},
        {"$set": {"content": doc.content}}
    )
    if result.modified_count == 0:
        raise HTTPException(
            status_code=400,
            detail="The document {path} don't exist!".format(path=doc.path)
        )
    return {"detail": "Successfully updated!"}


@app.delete("/document/", status_code=200)
async def delete_document(doc: Document):
    result = await db.document.delete_one({"path": doc.path})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=400,
            detail="The document {path} don't exist!".format(path=doc.path)
        )
    return {"detail": "Successfully deleted!"}
