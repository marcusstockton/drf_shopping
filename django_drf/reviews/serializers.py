from .models import Review
from rest_framework import serializers

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('url', 'id', 'title', 'description', 'rating', 'created_date', 'created_by', 'item')