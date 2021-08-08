from .models import Category, Languages, Words
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'is_active'
        ]


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = [
            'id',
            'language',
            'english_version',
            'translated_version',
            'definition',
        ]


class LanguageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = [
            'id',
            'name'
        ]
