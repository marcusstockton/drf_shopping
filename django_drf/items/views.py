from .models import Item
from reviews.models import Review
from reviews.serializers import ReviewSerializer

from attachments.models import Attachment
from attachments.serializers import AttachmentSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import action
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.request import Request

# curl -X PUT -H "Authorization: Token 049302cdb486c60001ea22969edee3f54ab4481b" -H "Content-Type: application/json" -d "{"title":"An updated third Item","description":"Some sales guff","price":"142.56","created_date":"2019-06-17T09:45:26.086009Z"}" "http://127.0.0.1:8000/items/5/"
class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        permission_classes = (IsAuthenticated,)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        permission_classes = (IsAuthenticated,)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        permission_classes = (IsAuthenticated,)
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        permission_classes = (IsAuthenticated,)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # @detail_route(methods=['get', 'post'])
    @action(detail=True, methods=['get', 'post'], serializer_class=ReviewSerializer)
    def reviews(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        queryset = Review.objects.filter(item=pk)
        serializer = ReviewSerializer(instance=queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    # @detail_route(methods=['get', 'post'])
    @action(detail=True, methods=['get', 'post'], serializer_class=AttachmentSerializer)
    def attachments(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        queryset = Attachment.objects.filter(item=pk)
        serializer = AttachmentSerializer(instance=queryset, many=True, context=serializer_context)
        return Response(serializer.data)
    

