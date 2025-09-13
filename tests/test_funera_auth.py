def test_crear_servicio_no_admin(client, monkeypatch):
    # Simular usuario con rol lector
    monkeypatch.setattr(
        "app.auth.get_current_user",
        lambda: {"username": "lector", "role": "lector"}
    )

    nuevo = {"id": 2, "nombre": "Servicio Básico", "precio": 500.0}
    response = client.post("/funeraria/", json=nuevo)
    assert response.status_code == 403
