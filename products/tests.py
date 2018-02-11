from django.test import TestCase
from django.db import IntegrityError

from products.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Hoodie", 
                               description="I love wearing hoodies.", 
                               price=5)

    def test_products_have_default_zero_quantity(self):
        """Products that do not have provided quantity will default to 0."""
        hoodie = Product.objects.get(name="Hoodie")
        self.assertEqual(hoodie.quantity, 0)

    def test_products_require_name_value(self):
        """Products that do not have provided name will not be added to db."""
        try:
            Product.objects.create(description="I love wearing sweaters.")
        except IntegrityError as e:
            pass
        except Exception as e:
            raise e

    def test_products_require_price_value(self):
        """Products that do not have provided price will not be added to db."""
        try:
            Product.objects.create(name="Sweater",
                               description="I love wearing sweaters.")
        except IntegrityError as e:
            pass
        except Exception as e:
            raise e
        

