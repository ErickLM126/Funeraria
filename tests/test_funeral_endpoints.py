def test_listar_vacio(client):
    response = client.get("/funeraria/")
    assert response.status_code == 200
    assert response.json() == []


def test_crear_servicio_admin(client, monkeypatch):
    monkeypatch.setattr(
        "app.auth.get_current_user",
        lambda: {"username": "admin", "role": "admin"}
    )

    nuevo = {"id": 1, "nombre": "Plan Premium", "precio": 1000.0}
    response = client.post("/funeraria/", json=nuevo)
    assert response.status_code == 200
    assert response.json()["nombre"] == "Plan Premium"


def test_obtener_servicio(client, monkeypatch):
    monkeypatch.setattr(
        "app.auth.get_current_user",
        lambda: {"username": "admin", "role": "admin"}
    )
    nuevo = {"id": 3, "nombre": "Plan Básico", "precio": 500.0}
    client.post("/funeraria/", json=nuevo)

    response = client.get("/funeraria/3")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Plan Básico"


def test_servicio_no_existente(client):
    response = client.get("/funeraria/999")
    assert response.status_code == 404
