from django.contrib.auth.models import User
from rest_framework import serializers

from bridleit.models import Word


class WordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Word
        fields = ('guess_word', 'taboo_words', 'data')
