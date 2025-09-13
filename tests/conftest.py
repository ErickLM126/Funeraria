import pytest
from starlette.testclient import TestClient
from app.main import app
from app import main   # 👈 importa el módulo con la lista de servicios


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def limpiar_servicios():
    """Limpia la lista de servicios antes de cada test"""
    main.servicios.clear()
