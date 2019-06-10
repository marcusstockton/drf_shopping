from .models import Attachment
from rest_framework import serializers

class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attachment
        #fields = ('url', 'id', 'title', 'description', 'price', 'created_date', 'created_by', 'updated_date', 'reviews')
        fields = "__all__"