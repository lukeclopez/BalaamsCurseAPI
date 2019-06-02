from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from bridleit.models import Word
from bridleit.serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    """
    Remember that when adding a word, the taboo words must be comma separated like so:
    Eve, First Man, Dust, Father 
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        )
