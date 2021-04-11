from news.models import News


def getting_news(request):
    news = News.objects.all()
    return {'news': news}
