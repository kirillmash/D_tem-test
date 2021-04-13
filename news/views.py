from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets

from .models import News
from .serializers import NewsSerializer


class NewsList(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def index(request):
    return render(request, 'base.html')


def get_list_users(request):
    users = User.objects.annotate(cnt=Count('news'))
    context = {
        "users": users
    }
    return render(request, 'users.html', context)
