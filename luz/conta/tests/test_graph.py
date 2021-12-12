import pytest
from http import HTTPStatus

from django.test import Client
from django.urls import reverse

from luz.base.django_assertions import assertion_contains


@pytest.fixture
def url(db):
    return reverse('graph', args=('chartjs',))


def test_page_status_code_200(client: Client, url):
    resp = client.get(url)

    assert resp.status_code == HTTPStatus.OK


def test_reverse(url):
    assert '/graph/chartjs' == url


def test_content(client: Client, url):
    resp = client.get(url)
    assertion_contains(resp, 'Chartjs')
