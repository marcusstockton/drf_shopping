from .models import Item
from reviews.serializers import ReviewSerializer
from attachments.serializers import AttachmentSerializer
from rest_framework import serializers
# from rest_framework.parsers import MultiPartParser, FormParser

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # parser_classes = (MultiPartParser, FormParser)
    class Meta:
        model = Item
        #fields = ('url', 'id', 'title', 'description', 'price', 'created_date', 'created_by', 'updated_date', 'reviews')
        fields = "__all__"