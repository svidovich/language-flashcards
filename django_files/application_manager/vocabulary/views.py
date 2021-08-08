import json

from distutils.util import strtobool

from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.db.utils import IntegrityError

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from vocabulary.models import Category, Words, Languages
from vocabulary.serializers import CategorySerializer, LanguageSeralizer, WordSerializer


class WordOperations(APIView):

    def get(self, request, format=None):
        parameters: dict = request.query_params.dict()
        language = str()
        try:
            language: str = parameters.pop('language')
        except KeyError:
            return Response(
                {'code': 400, 'message': 'Please specify language field'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        language_object: Languages = Languages.objects.get(name=language)
        word: QuerySet = Words.objects.filter(language=language_object, **parameters)
        serializer = WordSerializer(word, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        parameters: dict = request.query_params.dict()
        try:
            word = Words(**parameters)
            word.full_clean()
            word.save()
            return Response(
                {'code': 201, 'message': 'SUCCESS'},
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return Response(
                {'code': 400, 'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'code': 400, 'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class CategoryOperations(APIView):
    def get(self, request, format=None):
        parameters: dict = request.query_params.dict()
        # TODO
        # The way this works, if I use the all keyword in my request, I'll
        # get back an array; otherwise if I'm getting a category by name, I'll
        # get back an object. That is not very consistent; I think I should always
        # fork over an array. I should talk to an API expert about API design, and
        # get some opinions.
        try:
            if strtobool(parameters.get('all', 'false')):
                category_queryset: QuerySet = Category.objects.all()
                return Response(
                    [
                        CategorySerializer(category).data for category in category_queryset
                    ],
                    status=status.HTTP_200_OK
                )
            else:
                category_name: str = parameters.pop('name')
                category_object: Category = Category.objects.get(name=category_name, **parameters)
                return Response(CategorySerializer(category_object).data)
        except KeyError:
            return Response(
                {'code': 400, 'message': 'Please specify name field'},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request, format=None):
        parameters: dict = request.query_params.dict()
        try:
            category_name: str = parameters.pop('name')
            Category.objects.create(name=category_name, **parameters)
            return Response(
                {'code': 201, 'message': 'SUCCESS'},
                status=status.HTTP_201_CREATED
            )
        except KeyError:
            return Response(
                {'code': 400, 'message': 'Please specify name field'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError as e:
            return Response(
                {'code': 400, 'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class LanguageOperations(APIView):
    def get(self, request, format=None):
        parameters: dict = request.query_params.dict()
        try:
            language_name: str = parameters.pop('name')
            language_object = Languages.objects.get(name=language_name, **parameters)
            return Response(LanguageSeralizer(language_object).data)
        except KeyError:
            return Response(
                {'code': 400, 'message': 'Please specify name field'},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request, format=None):
        parameters: dict = request.query_params.dict()
        try:
            language_name: str = parameters.pop('name')
            Languages.objects.create(name=language_name, **parameters)
            return Response(
                {'code': 201, 'message': 'SUCCESS'},
                status=status.HTTP_201_CREATED
            )
        except KeyError:
            return Response(
                {'code': 400, 'message': 'Please specify name field'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError as e:
            return Response(
                {'code': 400, 'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class GetRandomWords(APIView):

    def get(self, request, format=None):
        parameters: dict = request.query_params.dict()
        if count := parameters.pop('count', None) is None:
            return Response(
                {'code': 400, 'message': 'Must specify desired word count'},
                status=status.HTTP_400_BAD_REQUEST
            )
        word: QuerySet = Words.objects.filter(**parameters).order_by('?')[:count+1]
        serializer = WordSerializer(word, many=True)
        return Response(serializer.data)
