import pytest
from mixer.backend.django import mixer
from OrderApp.models import Cart, CartItem
from rest_framework.test import APIClient
from ShopApp.models import Category, Product
from rest_framework.reverse import reverse
from django.test import TestCase

pytestmark = pytest.mark.django_db

class TestCategoryAPIViews(TestCase):

    def setUp(self):
        self.myclient = APIClient()

        print(self.myclient, "self.client")

    def test_category_list_works(self):
        #create a category
        cat1 = mixer.blend(Category, category="Clothing")
        cat2 = mixer.blend(Category, category="Accessories")

        url = reverse("category_list_api")

        #call the url
        response = self.myclient.get(url)

        #assertions
        #-json
        #-status code
        assert response.json != None

        assert len(response.json()) == 4

        assert response.status_code == 200