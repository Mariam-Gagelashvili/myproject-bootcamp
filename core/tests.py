from django.test import TestCase
import pytest
from rest_framework.test import APIClient
# Create your tests here.

@pytest.mark.django_db
def test_product_list():
    client = APIClient()
    response = client.get('/products/')
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_post_list():
    client = APIClient()
    response = client.get('/posts/')
    assert response.status_code == 200