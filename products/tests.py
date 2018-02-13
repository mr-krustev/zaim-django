from django.test import TestCase
from django.db import IntegrityError

from products.models import Product

class ProductTestCase(TestCase):
    prod_name = "Hoodie"
    prod_description = "I love hoodies."
    prod_price = 5

    def createProduct(self, name=prod_name, description=prod_description,
                      price=prod_price):
        return Product.objects.create(name=name, description=description,
                                      price=price)

    def test_creating_product_should_work_with_sufficient_data(self):
        try:
            self.createProduct()
        except Exception as e:
            self.fail("Product.Create() raised unexpected %s." % e)

    def test_creating_products_with_no_name_should_fail(self):
        """Products that do not have provided name will not be added to db."""
        with self.assertRaises(IntegrityError):
            Product.objects.create(description="I love wearing sweaters.",
                                   price=5)

    def test_creating_products_with_no_price_should_fail(self):
        """Products that do not have provided price will not be added to db."""
        with self.assertRaises(IntegrityError):
                Product.objects.create(name="Test")

    def test_creating_products_with_empty_name_should_fail(self):
        self.fail("Not implemented.")

    def test_creating_products_with_empty_descrption_should_work(self):
        self.fail("Not implemented.")

    def test_created_product_should_have_provided_values(self):
        result = self.createProduct()
        self.assertEqual(result.name, self.prod_name)
        self.assertEqual(result.description, self.prod_description)
        self.assertEqual(result.price, self.prod_price)

    def test_created_products_should_have_default_quantity_of_zero(self):
        """Products that do not have provided quantity will default to 0."""
        hoodie = self.createProduct()
        self.assertEqual(hoodie.quantity, 0)
