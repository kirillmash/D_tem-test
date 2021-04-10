from rest_framework import generics, viewsets

from .models import News
from .serializers import NewsSerializer


class NewsList(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

