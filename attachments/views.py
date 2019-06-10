from .models import Attachment
from rest_framework import viewsets
from .serializers import AttachmentSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attachments to be viewed or edited.
    """
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

