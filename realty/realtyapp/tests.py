from django.test import TestCase
from mixer.backend.django import mixer
from .models import *

# Create your tests here.
class MetroTestCase(TestCase):
    def setUp(self):
        self.metro = mixer.blend(Metro, name='metro_test')

    def test_metro_str(self):
        self.assertEqual(self.metro.name, 'metro_test')

class Room_countTestCase(TestCase):
    def setUp(self):
        self.room_count = mixer.blend(Metro, name='room_test')

    def test_room_str(self):
        self.assertEqual(self.room_count.name, 'room_test')

class MaterialTestCase(TestCase):
    def setUp(self):
        self.material = mixer.blend(Material, name='material_test')

    def test_material_str(self):
        self.assertEqual(self.material.name, 'material_test')

class BalconyTestCase(TestCase):
    def setUp(self):
        self.balcony = mixer.blend(Balcony, name='balcony_test')

    def test_balcony_str(self):
        self.assertEqual(self.balcony.name, 'balcony_test')

class CurrencyTestCase(TestCase):
    def setUp(self):
        self.currency = mixer.blend(Currency, name='currency_test')

    def test_currency_str(self):
        self.assertEqual(self.currency.name, 'currency_test')

class StreetTestCase(TestCase):
    def setUp(self):
        self.street = mixer.blend(Street, name='street_test')

    def test_street_str(self):
        self.assertEqual(self.street.name, 'street_test')

class SityTestCase(TestCase):
    def setUp(self):
        self.sity = mixer.blend(Sity, name='sity_test')

    def test_sity_str(self):
        self.assertEqual(self.sity.name, 'sity_test')

class Area_cityTestCase(TestCase):
    def setUp(self):
        self.area_city = mixer.blend(Area_city, name='area_city_test')

    def test_area_city_str(self):
        self.assertEqual(self.area_city.name, 'area_city_test')

class CategoryTestCase(TestCase):

    def test_area_city_str(self):
        self.category = mixer.blend(Category, name='sale')
        self.assertEqual(self.category.name, 'sale')


        self.category = mixer.blend(Category, name='rent')
        self.assertEqual(self.category.name, 'rent')

