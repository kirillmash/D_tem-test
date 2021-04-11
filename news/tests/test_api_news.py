from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import News


class NewsApiTestCase(APITestCase):
    def get_test(self):
        url = reverse('news_list')
        response = self.client.get(url)
        print(response)