from django.urls import path, include
from .views import PostList, PostDetail
from rest_framework import routers

app_name = "blog_api"



urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate')
]