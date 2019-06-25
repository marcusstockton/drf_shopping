from .models import Review
from rest_framework import viewsets, renderers
from rest_framework.decorators import api_view, action
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    