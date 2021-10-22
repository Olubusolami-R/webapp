from django.test import TestCase
from .models import Pet

class PetModelTests(TestCase):
    def setUp(self):
        Pet.objects.create(name="Chihuahua",hair="short", size="small")

    def test_hair(self):
        chi = Pet.objects.get(name="Chihuahua")
        self.assertEqual(chi.hair, "short")

# Create your tests here.
