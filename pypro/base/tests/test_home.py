# from django.test import Client
#
#
# def test_status_code(client: Client):
#     resp = client.get('/')
#     assert resp.status_code == 200
import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
