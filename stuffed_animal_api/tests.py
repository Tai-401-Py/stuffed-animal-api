from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import StuffedAnimal


class AnimalTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_thing = StuffedAnimal.objects.create(
            owner=testuser1,
            name="Luna Moth",
            manufacturer="Squishable",
            description="A rosey squishable friend to carry you through.",
        )
        test_thing.save()

    def test_things_model(self):
        stuffed_animal = StuffedAnimal.objects.get(id=1)
        actual_owner = str(stuffed_animal.owner)
        actual_name = str(stuffed_animal.name)
        actual_description = str(stuffed_animal.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Luna Moth")
        self.assertEqual(
            actual_description, "A rosey squishable friend to carry you through."
        )

    def test_get_stuffed_animal_list(self):
        url = reverse("stuffed_animal_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0]["name"], "Luna Moth")

    def test_get_thing_by_id(self):
        url = reverse("stuffed_animal_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        stuffed_animal = response.data
        self.assertEqual(stuffed_animal["name"], "Luna Moth")

    def test_create_thing(self):
        url = reverse("stuffed_animal_list")
        data = {"owner": 1, "name": "spoon", "manufacturer": "Toy Bin", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        things = StuffedAnimal.objects.all()
        self.assertEqual(len(things), 2)
        self.assertEqual(StuffedAnimal.objects.get(id=2).name, "spoon")

    def test_update_thing(self):
        url = reverse("stuffed_animal_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "Luna Moth",
            "manufacturer": "Squishable",
            "description": "Limited Edition no way!",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        stuffed_animal = StuffedAnimal.objects.get(id=1)
        self.assertEqual(stuffed_animal.name, data["name"])
        self.assertEqual(stuffed_animal.owner.id, data["owner"])
        self.assertEqual(stuffed_animal.description, data["description"])

    def test_delete_thing(self):
        url = reverse("stuffed_animal_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        things = StuffedAnimal.objects.all()
        self.assertEqual(len(things), 0)
