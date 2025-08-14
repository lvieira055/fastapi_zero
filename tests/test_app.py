from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: act     - Execute(o SUT)
    - Assert     - Garanta que X é X
    """
    # arrange
    client = TestClient(app)
    # act
    response = client.get('/')
    # Assert
    assert response.json() == {'message': 'Olá Mundo!'}

    assert response.status_code == HTTPStatus.OK
