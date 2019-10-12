from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


# utils
def extract_keys(old_dict, *args):
    return {key: value for key, value in old_dict.items() if key in args}


# tests
def test_get_inexistent_document():
    response = client.get("/minha_pagina")
    assert response.status_code == 404

    assert response.json() == {
        "detail": "The document minha_pagina don't exist!"
    }


def test_create_new_document():
    response = client.post("/minha_pagina")
    assert response.status_code == 201

    assert "_id" in response.json().keys()
