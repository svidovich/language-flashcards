import json

from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from vocabulary.models import Words
from vocabulary.serializers import WordSerializer

class WordList(APIView):

    def get(self, request, format=None):
        # Get all of the words
        words = Words.objects.all()
        # Serialize them to JSON
        serializer = WordSerializer(words, many=True)
        # Return a response object
        return Response(serializer.data)

    def post(self, request, format=None):
        # Serialize the data from the post
        serializer = WordSerializer(data=request.data)
        # Handy!
        if serializer.is_valid():
            # If they failed to suck, create the data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Otherwise tell them they sucked
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetWord(APIView):

    def get(self, request, format=None):
        parameters: dict = request.query_params.dict()
        word: QuerySet = Words.objects.filter(**parameters)
        serializer = WordSerializer(word, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        parameters: dict = request.query_params.dict()
        try:
            word = Words(**parameters)
            word.full_clean()
            word.save()
            return Response(status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(
                json.dumps({'code': 400, 'message': e.message_dict}),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                json.dumps({'code': 400, 'message': f'{e}'}),
                status=status.HTTP_400_BAD_REQUEST
            )


class GetRandomWords(APIView):

    def get(self, request, format=None):
        parameters: dict = request.query_params.dict()
        if count := parameters.pop('count', None) is None:
            return Response(json.dumps({'code': 400, 'message': 'Must specify desired word count'}), status=status.HTTP_400_BAD_REQUEST)
        word: QuerySet = Words.objects.filter(**parameters).order_by('?')[:count]
        serializer = WordSerializer(word, many=True)
        return Response(serializer.data)