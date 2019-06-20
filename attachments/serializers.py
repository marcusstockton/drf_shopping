from .models import Attachment
from items.models import Item
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files import File
import base64

class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    parser_classes = (MultiPartParser, FormParser)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = Attachment
        fields = ('url', 'id', 'image', 'item', 'created_by', 'base64_image')
        #fields = "__all__"

    def get_base64_image(self, obj):
        f = open(obj.image.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data