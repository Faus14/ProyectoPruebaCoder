
from django.urls import path

from .views import curso


urlpatterns = [
    path('agregacurso/<nombre>/<canada>', curso),
]
