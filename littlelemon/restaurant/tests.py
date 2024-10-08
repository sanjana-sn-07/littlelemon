from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import menuSerializer
from rest_framework.response import Response
from decimal import Decimal

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Ice-cream', price=10.5, inventory=50)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(item.title, 'Ice-cream')
        self.assertEqual(item.price, Decimal(10.5))
        self.assertEqual(item.inventory, 50)

class MenuViewTest(TestCase):
    def setup(self):  
        roti = Menu.objects.create(title='Roti', price=4, inventory=30)
        naan = Menu.objects.create(title='Naan', price=5.5, inventory=30)
        kulcha = Menu.objects.create(title='Kulcha', price=5.5, inventory=20)

    def test_get_all(self):
        self.setup()
        items = Menu.objects.all()
        for item in items:
            serializer = menuSerializer(item)
            response= Response(serializer.data)
            self.assertEqual(serializer.data, response.data)
    