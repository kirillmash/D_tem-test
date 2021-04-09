from django.urls import path
from .views import NewsList

urlpatterns = [
    path('news_list/', NewsList.as_view({'get': 'list'})),
    path('news_list/<int:pk>/', NewsList.as_view({'get': 'retrieve'})),
    path('add_news/', NewsList.as_view({'post': 'create'})),
    path('update_news/<int:pk>/', NewsList.as_view({'put': 'update'})),
    path('delete_news/<int:pk>/', NewsList.as_view({'delete': 'destroy'})),

]