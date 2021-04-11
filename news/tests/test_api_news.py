import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import News
from ..serializers import NewsSerializer


class NewsApiTestCase(APITestCase):
    def setUp(self):
        self.news1 = News.objects.create(title='Test News 1', content='Contest Test 1')
        self.news2 = News.objects.create(title='Test News 2', content='Contest Test 2')

    def test_get(self):
        url = reverse('news_list')
        response = self.client.get(url)
        serializer_data = NewsSerializer([self.news1, self.news2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(2, News.objects.all().count())
        url = reverse('add_news')
        data = {
            "title": "test news 1",
            "content": "news for test 1"
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, News.objects.all().count())

    def test_update(self):
        url = reverse('update_news', args=(self.news1.id,))
        data = {
            "title": self.news1.title,
            "content": "news for test 1 updated"
        }
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.news1.refresh_from_db()
        self.assertEqual("news for test 1 updated", self.news1.content)

    def test_delete(self):
        self.assertEqual(2, News.objects.all().count())
        url = reverse('delete_news', args=(self.news1.id,))
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, News.objects.all().count())
