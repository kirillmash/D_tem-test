import random
import string

from celery import shared_task

from .models import News


@shared_task
def create_new_news():
    random_news_title = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    random_news_content = ' '.join([random.choice(string.ascii_letters) for _ in range(100)])
    new_news = News.objects.create(title=random_news_title, content=random_news_content)
    return new_news.title
