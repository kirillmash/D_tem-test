from django.shortcuts import render
from rest_framework import viewsets

from .models import News
from .serializers import NewsSerializer


class NewsList(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def index(request):
    return render(request, 'base.html')
