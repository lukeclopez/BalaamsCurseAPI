from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from bridleit.models import Word
from bridleit.serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        )
