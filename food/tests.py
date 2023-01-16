from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Food

class FoodTestCase(TestCase):
    def setUp(self):
        Food.objects.create(name="Donuts", description="Homer")
        Food.objects.create(name="Frites", description="Tuches")

    def test_food(self):
        donut = Food.objects.get(name="Donuts")
        frite = Food.objects.get(name="Frites")
        self.assertEqual(donut.name, 'Donuts')
        self.assertEqual(frite.name, 'Frites')