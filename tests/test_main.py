from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


# utils
def extract_keys(old_dict, *args):
    return {key: value for key, value in old_dict.items() if key in args}


# tests
def test_create_new_document():
    response = client.get("/minha_pagina")
    assert response.status_code == 200

    useful_items = extract_keys(
        response.json(),
        "path", "content", "password"
    )
    assert useful_items == {
        "path": "minha_pagina",
        "content": "",
        "password": "",
    }
