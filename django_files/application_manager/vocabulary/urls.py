from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from vocabulary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vocabulary/word', views.WordOperations.as_view()),
    path('vocabulary/random', views.GetRandomWords.as_view()),
    path('vocabulary/languages', views.LanguageOperations.as_view()),
    path('vocabulary/categories', views.CategoryOperations.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
