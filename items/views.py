from .models import Item
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework import viewsets
from rest_framework.decorators import action, detail_route
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.request import Request



class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # @action(detail=True, methods=['get'])
    @detail_route(methods=['get'])
    def reviews(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        queryset = Review.objects.filter(item=pk)
        serializer = ReviewSerializer(instance=queryset, many=True, context=serializer_context)
        return Response(serializer.data)