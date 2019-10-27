from fastapi import FastAPI, HTTPException
from starlette.responses import Response
from starlette.middleware.cors import CORSMiddleware

from app.database import db
from app.config import FRONTEND_ORIGIN

from datetime import datetime
from typing import List
from pydantic import BaseModel


class Document(BaseModel):
    _id: str = None
    path: str
    content: str = ""
    child:  List[str] = []
    created_at: datetime = None


app = FastAPI()

origins = [
    FRONTEND_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/get_last_updated/{file_path:path}", status_code=200)
async def get_last_updated(file_path: str):
    requested_doc = await db.document.find_one({"path": file_path})
    if requested_doc is None:
        raise HTTPException(
            status_code=404,
            detail="The document {path} don't exist!".format(path=file_path)
        )
    return {"last_updated": requested_doc["last_updated"]}


@app.post("/document/", status_code=201)
async def insert_document(doc: Document):
    alredy_on_db = await db.document.find_one({"path": doc.path}) is not None
    if alredy_on_db:
        raise HTTPException(
            status_code=409,
            detail="The document {path} alredy exist!".format(path=doc.path)
        )

    datetime_utc_now = datetime.utcnow()

    list_path = doc.path.split("/")
    if len(list_path) > 1:
        new_child = list_path.pop()

        last_child = new_child
        while len(list_path) > 0:
            parent_path = "/".join(list_path)
            parent = await db.document.find_one({"path": parent_path})
            if parent is None:
                await db.document.insert_one({
                    "path": parent_path,
                    "content": "",
                    "child": [last_child],
                    "created_at": datetime_utc_now,
                    "last_updated": datetime_utc_now
                })
            else:
                if last_child not in parent["child"]:
                    parent["child"].append(last_child)
                    await db.document.update_one(
                        {"path": parent_path},
                        {"$set": {"child": parent["child"]}}
                    )
            last_child = list_path.pop()

    default_new_doc = {
        "path": doc.path,
        "content": "",
        "child": [],
        "created_at": datetime_utc_now,
        "last_updated": datetime_utc_now
    }
    result = await db.document.insert_one(default_new_doc)
    return {"_id": str(result.inserted_id), "created_at": datetime_utc_now}


@app.put("/document/", status_code=200)
async def update_document(doc: Document):
    doc_dont_exist = await db.document.find_one({"path": doc.path}) is None
    if doc_dont_exist:
        raise HTTPException(
            status_code=400,
            detail="The document {path} don't exist!".format(path=doc.path)
        )

    datetime_utc_now = datetime.utcnow()
    await db.document.update_one(
        {"path": doc.path},
        {"$set": {"content": doc.content, "last_updated": datetime_utc_now}}
    )
    return {
        "detail": "Successfully updated!",
        "last_updated": datetime_utc_now
    }


@app.delete("/document/", status_code=200)
async def delete_document(doc: Document):
    result = await db.document.delete_one({"path": doc.path})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=400,
            detail="The document {path} don't exist!".format(path=doc.path)
        )
    return {"detail": "Successfully deleted!"}
