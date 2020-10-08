# from django.test import Client
#
#
# def test_status_code(client: Client):
#     resp = client.get('/')
#     assert resp.status_code == 200
import pytest
# from django.test import TestCase
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_uses_home_template(resp):  # Example - List Comprehension
    assert 'base/home.html' in [template.name for template in resp.templates]


def test_list(resp):  # Example - Without List Comprehension
    templates_usados = []
    for template in resp.templates:
        templates_usados.append(template.name)
    assert 'base/home.html' in templates_usados

# class HomePageTest(TestCase):  # Página 48
#     def test_uses_home_template(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'base/home.html')
#
#     def test_title_home_template(self):
#         response = self.client.get('/')
#         self.assertContains(response, '<title>Atacadão Python Pro - Home</title>')

# class HomePageTest2(TestCase):
#     def test_title_home_template(self):
#         response = self.client.get('/')
#         self.assertContains(response, '<title>Atacadão Python Pro</title>')
