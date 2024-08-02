

import json

import pytest
from django.test import Client
from django.urls import reverse

from product.models import Brand, Category, Product


# Create your tests here.
@pytest.mark.django_db
class TestProdect:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()
        self.brand = Brand.objects.create(name='brand1')
        self.category = Category.objects.create(name='category1')
        self.url_list = "product-list"
        self.url_detail = "product-detail"
        self.product_objects = Product.objects.create(
            name="Product1",
            description="this is Product1",
            is_digital=True,
            brand=self.brand,
            category=self.category)

    def test_list_prodect(self):
        response = self.client.get(reverse(self.url_list))
        assert response.status_code == 200

    def test_create_product(self):
        data = {
            "name": "Product1",
            "description": "this is Product1",
            "is_digital": True,
            "brand": self.brand.id,
            "category": self.category.id,
        }
        response = self.client.post(reverse(
            self.url_list),
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 201

    def test_update_product(self):
        update_data = {
            "name": "Product2",
            "description": "this is Product2",
            "is_digital": True,
            "brand": self.brand.id,
            "category": self.category.id,
        }
        response = self.client.put(reverse(
            self.url_detail,
            args=[self.product_objects.id]),
            data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200

    def test_delete_product(self):
        response = self.client.delete(reverse(
            self.url_detail,
            args=[self.product_objects.id]))
        assert response.status_code == 204

    def test_retrieve_exam(self):
        update_data = {
            "name": "Product3",
            "description": "this is Product1",
            "is_digital": True,
            "brand": self.brand.id,
            "category": self.category.id,
        }
        response = self.client.patch(reverse(
            self.url_detail,
            args=[self.product_objects.id]),
            data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200
