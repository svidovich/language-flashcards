from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from vocabulary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vocabulary/', views.WordList.as_view()),
    path('vocabulary/word', views.GetWord.as_view()),
    path('vocabulary/random', views.GetRandomWords.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

