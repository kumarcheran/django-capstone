from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_setUp(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        print(str(item))
        self.assertEqual(str(item), "IceCream : 80")

