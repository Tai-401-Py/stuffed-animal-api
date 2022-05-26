from django.urls import path
from .views import StuffedAnimalList, StuffedAnimalDetail

urlpatterns = [
    path("", StuffedAnimalList.as_view(), name="stuffed_animal_list"),
    path("<int:pk>/", StuffedAnimalDetail.as_view(), name="stuffed_animal_detail"),
]