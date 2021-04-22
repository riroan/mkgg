from django.urls import path
from . import views

app_name = "search"

urlpatterns = [
    path('', views.index),
    path('userInfo', views.searchUser, name="searchUser"),
    path('create', views.searchCreate, name="searchCreate"),
    path('test', views.test, name="test"),
    path("test2", views.test2),
]
