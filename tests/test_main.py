from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


# utils
def extract_keys(old_dict, *args):
    return {key: value for key, value in old_dict.items() if key in args}


# tests
def test_get_inexistent_document():
    response = client.get("document/minha_pagina")
    assert response.status_code == 404

    assert response.json() == {
        "detail": "The document minha_pagina don't exist!"
    }


def test_create_new_document():
    response = client.post(
        "/document/",
        json={"path": "minha_pagina"}
    )
    assert response.status_code == 201

    assert "_id" in response.json().keys()


def test_get_document():
    response = client.get("document/minha_pagina")
    assert response.status_code == 200

    useful_response = extract_keys(
        response.json(),
        "path", "content", "password"
    )
    assert useful_response == {
        "path": "minha_pagina",
        "content": "",
        "password": ""
    }


def test_insert_existent_document():
    response = client.post(
        "/document/",
        json={"path": "minha_pagina"}
    )
    assert response.status_code == 409

    assert response.json() == {
        "detail": "The document minha_pagina alredy exist!"
    }
