from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from vocabulary import views

router = routers.DefaultRouter()
router.register(r'vocabulary', views.WordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # what does this do
    path('vocabulary/', include('rest_framework.urls', namespace='rest_framwork'))
]


