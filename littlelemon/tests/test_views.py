from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import menuSerializer
from rest_framework.response import Response

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
    