import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from testdb.models import Operation

@pytest.mark.django_db
def test_create_operation():
    client = APIClient()
    url = reverse()


# @pytest.mark.django_db
# def test_example(client):
#     response = client.get('/catergories/')
#     assert response.status_code == 200

#test_example()