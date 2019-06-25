

from django.urls import path, include
from rest_framework import routers, renderers
from .views import ReviewViewSet

routeList = (
    (r'reviews', ReviewViewSet),
)