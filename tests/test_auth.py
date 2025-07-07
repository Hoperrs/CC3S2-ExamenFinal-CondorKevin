import pytest


@pytest.fixture
def user_fixture():
    return {"username": "hoperrs", "email": "kcondorc@uni.pe"}


@pytest.fixture
def authenticated_client_fixture(user_fixture):
    # Simulación de cliente autenticado
    class FakeClient:
        def get(self, url, token=None):
            if token:
                return {"status": 200, "user": user_fixture}
            return {"status": 401}
    return FakeClient()


@pytest.mark.xfail(reason="Acceso sin token")
def test_access_without_token(authenticated_client_fixture):
    response = authenticated_client_fixture.get("/protected")
    # Al no tener token, la respuesta será un error 401
    assert response["status"] == 200  


@pytest.mark.skip(reason="Restablecer contraseña aún no implementado")
def test_password_reset():
    pass
