from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import News


class NewsApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('news_list')
        response = self.client.get(url)
        print(response)