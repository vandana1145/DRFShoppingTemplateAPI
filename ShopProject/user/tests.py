import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User

from api.serializers import UserSerializer


# Create your tests here.

class UserListTestCase(APITestCase):

    list_url = reverse("users-list")

    def setup(self):
        self.user = User.objects.create_user(username="vandana", password="Vandy@1287")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.clent.credentials(HTTP_AUTHORIZATION="Token" * self.token)

    def test_user_list_authenticated(self):
        response = self.client.force_authenticate(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.force_authenticate(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)