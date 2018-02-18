from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from products.models import Product


class ProductTestCase(TestCase): # pragma: no cover
    prod_name = "Hoodie"
    prod_description = "I love hoodies."
    prod_price = 5

    @staticmethod
    def createProduct(name=prod_name, description=prod_description,
                      price=prod_price):
        return Product.objects.create(name=name, description=description,
                                      price=price)

    def test_creating_product_with_sufficient_data_should_succeed(self):
        try:
            product = self.createProduct()
            product.save()
        except Exception as e:
            self.fail("Product.Create() raised unexpected %s." % e)

    def test_creating_products_with_null_name_should_fail(self):
        """Products that do not have provided name will not be added to db."""
        with self.assertRaises(IntegrityError):
            Product.objects.create(name=None, description="I love wearing sweaters.",
                                   price=5)

    def test_creating_products_with_empty_name_should_fail(self):
        with self.assertRaises(IntegrityError):
            Product.objects.create(price=5)

    def test_creating_products_with_no_price_should_fail(self):
        """Products that do not have provided price will not be added to db."""
        with self.assertRaises(IntegrityError):
            Product.objects.create(name="Test")

    def test_creating_products_with_empty_description_should_work(self):
        try:
            product = Product.objects.create(name="One", price=1)
            product.save()
        except Exception as e:
            self.fail("Product.Create() raised unexpected %s." % e)
        self.assertEqual(product.description, "")

    def test_creating_products_with_correct_product_type_should_work(self):
        try:
            Product.objects.create(name=self.prod_name,description=self.prod_description,price=self.prod_price, product_type="T")
        except Exception as e:
            self.fail("Product.Create() raised unexpected %s." % e)

    def test_creating_products_with_wrong_product_type_should_fail(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(name=self.prod_name, description=self.prod_description, price=self.prod_price,
                                             product_type="Q")

    def test_creating_products_with_long_product_type_should_fail(self):
        with self.assertRaises(ValidationError):
            Product.objects.create(name=self.prod_name, description=self.prod_description, price=self.prod_price,
                                             product_type='ClothesJewels')

    def test_created_product_should_have_provided_values(self):
        result = self.createProduct()
        self.assertEqual(result.name, self.prod_name)
        self.assertEqual(result.description, self.prod_description)
        self.assertEqual(result.price, self.prod_price)

    def test_created_product_should_have_default_quantity_of_zero(self):
        """Products that do not have provided quantity will default to 0."""
        hoodie = self.createProduct()
        self.assertEqual(hoodie.quantity, 0)

    def test_created_product_get_absolute_url_should_return_correct_url(self):
        p = self.createProduct()
        absolute_url = p.get_absolute_url()
        self.assertEqual(absolute_url, '/products/' + str(p.product_id) + '/')
