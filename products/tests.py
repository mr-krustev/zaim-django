from django.test import TestCase
from products.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Hoodie", description="I love wearing hoodies.", price=5)

    def test_products_have_default_zero_quantity(self):
        """Products that do not have provided quantity will default to 0."""
        hoodie = Product.objects.get(name="Hoodie")
        self.assertEqual(hoodie.quantity, 0)