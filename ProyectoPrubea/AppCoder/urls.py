
from django.urls import path

from .views import curso


urlpatterns = [
    path('AppCoder/agregacurso/<nombre>/<canada>', curso),
]
