from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from vocabulary.models import Words
from vocabulary.serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to get words data by word
    """
    queryset = Words.objects.all().order_by('english_version')
    serializer_class = WordSerializer

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Words.objects.all()
        serializer = WordSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)