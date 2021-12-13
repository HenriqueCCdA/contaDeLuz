import pytest
from http import HTTPStatus

from django.test import Client
from django.urls import reverse

from luz.base.django_assertions import assertion_contains


@pytest.fixture
def url():
    return reverse('graph', args=('chartjs',))


@pytest.fixture
def response(client: Client, url, db):
    return client.get(url)


def test_page_status_code_200(response):
    assert response.status_code == HTTPStatus.OK


def test_reverse(url):
    assert '/graph/chartjs' == url


def test_content(response):
    assertion_contains(response, 'Chartjs')


def test_graph_navbar(response):
    assertion_contains(response, '<a class="nav-link active" href="/graph/chartjs">Chartjs</a>')
