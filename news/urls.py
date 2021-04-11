from django.urls import path
from .views import NewsList, index

urlpatterns = [
    path('index/', index),
    path('news_list/', NewsList.as_view({'get': 'list'}), name='news_list'),
    path('news_list/<int:pk>/', NewsList.as_view({'get': 'retrieve'}), name='news_detail'),
    path('add_news/', NewsList.as_view({'post': 'create'}), name='add_news'),
    path('update_news/<int:pk>/', NewsList.as_view({'put': 'update'}), name='update_news'),
    path('delete_news/<int:pk>/', NewsList.as_view({'delete': 'destroy'}), name='delete_news'),


]