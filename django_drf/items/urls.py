

from django.urls import path, include
from rest_framework import routers
from . import views

routeList = (
    (r'items', views.ItemViewSet),
)