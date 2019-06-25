

from django.urls import path, include
from rest_framework import routers
from . import views

routeList = (
    (r'users', views.UserViewSet),
    (r'groups', views.GroupViewSet),
)
