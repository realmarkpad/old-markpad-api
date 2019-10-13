from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


# utils
def extract_keys(old_dict, *args):
    return {key: value for key, value in old_dict.items() if key in args}


# tests
def test_get_inexistent_document():
    res = client.get("document/minha_pagina")
    assert res.status_code == 404
    assert res.json() == {
        "detail": "The document minha_pagina don't exist!"
    }


def test_create_new_document():
    res = client.post(
        "/document/",
        json={"path": "minha_pagina"}
    )
    assert res.status_code == 201
    assert "_id" in res.json().keys()


def test_get_document():
    res = client.get("document/minha_pagina")
    assert res.status_code == 200

    useful_res = extract_keys(
        res.json(),
        "path", "content", "password"
    )
    assert useful_res == {
        "path": "minha_pagina",
        "content": "",
        "password": ""
    }


def test_insert_document_alredy_exist():
    res = client.post(
        "/document/",
        json={"path": "minha_pagina"}
    )
    assert res.status_code == 409
    assert res.json() == {
        "detail": "The document minha_pagina alredy exist!"
    }


def test_update_document():
    res = client.put(
        "/document/",
        json={"path": "minha_pagina", "content": "Opa!"}
    )
    assert res.status_code == 200
    assert res.json() == {
        "detail": "Successfully updated"
    }

    res_get = client.get("document/minha_pagina")
    assert res_get.status_code == 200
    useful_res = extract_keys(res_get.json(), "content")
    assert useful_res == {"content": "Opa!"}


def test_update_inexistent_document():
    res = client.put(
        "/document/",
        json={"path": "nao_existe"}
    )
    assert res.status_code == 400
    assert res.json() == {
        "detail": "The document nao_existe don't exist!"
    }
