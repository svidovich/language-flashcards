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

class WordByEnglishVersion(APIView):

    def get(self, request, format=None):
        parameters = request.query_params
        word = []
        # Downselect by language, if it's there, then by word
        if language := parameters.get('language'):
            word = Words.objects.filter(language=language)
        if english_version := parameters.get('english_version'):
            word = word.filter(english_version=english_version)
        serializer = WordSerializer(word, many=True)
        return Response(serializer.data)

# You can also do it like this. It abstracts away all of the request / response handling logic
# and does things more concisely, but is fairly opaque.
from rest_framework import generics
class WordListGeneric(generics.ListCreateAPIView):
    queryset = Words.objects.all()
    serializer_class = WordSerializer