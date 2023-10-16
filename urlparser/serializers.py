from .models import ShortenedURL
from rest_framework import serializers

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ('url', 'short_url', 'creation_date')