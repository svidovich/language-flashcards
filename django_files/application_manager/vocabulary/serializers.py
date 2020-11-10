from .models import Words
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = [
            'id'
            'language'
            'english_version'
            'translated_version'
            'definition'
        ]
