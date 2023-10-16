from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ShortenedURL
from .serializers import ShortenedURLSerializer

import uuid

@api_view(['POST'])
def shorten_url(request):
    data = request.data
    data['short_url'] = uuid.uuid4().hex[:6].upper()
    serializer = ShortenedURLSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'shortUrl': serializer.data['short_url']}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def redirect_url(request, short_url):
    shortened_url = ShortenedURL.objects.filter(short_url=short_url).first()
    if shortened_url is None:
        return Response(status=404, data={'message': 'Short URL not found'})
    return HttpResponseRedirect(shortened_url.url)