from .models import *
from .serializers import*
from rest_framework.viewsets import ModelViewSet


class MovieView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer