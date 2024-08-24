from django.test import TestCase
from decimal import Decimal
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Ice-cream', price=10.5, inventory=50)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(item.title, 'Ice-cream')
        self.assertEqual(item.price, Decimal(10.5))
        self.assertEqual(item.inventory, 50)