
from django.urls import path

from .views import curso1, entregables, estudiantes, inicio, profesores


urlpatterns = [
    path('', inicio),
    path('agregacurso/<nombre>/<canada>', curso1),
    path('profesores', profesores),
    path('estudiantes', estudiantes),
    path('entregables', entregables),
]
