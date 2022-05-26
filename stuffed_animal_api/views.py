
from rest_framework import generics
from .serializers import StuffedAnimalSerializer
from .models import StuffedAnimal

# Create your views here.

class StuffedAnimalList(generics.ListCreateAPIView):

    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    # Serializer_class
    queryset = StuffedAnimal.objects.all()
    serializer_class = StuffedAnimalSerializer


# The ThingDetail needs the same things
class StuffedAnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StuffedAnimal.objects.all()
    serializer_class = StuffedAnimalSerializer