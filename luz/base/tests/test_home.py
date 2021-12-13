import pytest
from http import HTTPStatus

from django.test import Client

from luz.base.django_assertions import assertion_contains


@pytest.fixture
def response(client: Client):
    return client.get('/')


def test_home_status_code(response):
    assert response.status_code == HTTPStatus.OK


def test_home_navbar(response):
    assertion_contains(response, '<a class="nav-link active" href="/"> Home </a>')
