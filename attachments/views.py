from .models import Attachment
from rest_framework import viewsets, renderers
from .serializers import AttachmentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class AttachmentModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attachments to be viewed or edited.
    """
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer







class AttachmentViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        serializer_context = {
            'request': request,
        }
        queryset = Attachment.objects.all()
        serializer = AttachmentSerializer(queryset,context=serializer_context, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        queryset = Attachment.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AttachmentSerializer(user,context=serializer_context)
        return Response(serializer.data)




