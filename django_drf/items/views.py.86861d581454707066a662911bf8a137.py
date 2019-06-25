from .models import Item
from reviews.models import Review
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.request import Request



class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        serializer_context = {
    'request': Request(request),
}
        #breakpoint()
        queryset = Review.objects.filter(item=pk)
        serializer = ItemSerializer(instance=queryset, many=True)
        return Response(serializer.data)