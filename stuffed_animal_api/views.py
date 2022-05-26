
from rest_framework import generics
from .serializers import StuffedAnimalSerializer
from .models import StuffedAnimal

# Create your views here.

class StuffedAnimalList(generics.ListCreateAPIView):
    queryset = StuffedAnimal.objects.all()
    serializer_class = StuffedAnimalSerializer


class StuffedAnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StuffedAnimal.objects.all()
    serializer_class = StuffedAnimalSerializer