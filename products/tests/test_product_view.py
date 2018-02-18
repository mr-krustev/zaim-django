from django.test import TestCase

from products.models import Product
from django.urls import reverse


class ProductViewTest(TestCase): # pragma: no cover
    prod_name = 'Test Name'
    prod_description = 'Test Description'

    @classmethod
    def setUpTestData(cls):
        # Create some products.
        number_of_products = 5
        for product_num in range(number_of_products):
            Product.objects.create(name=cls.prod_name + ' ' + str(product_num),
                                   description=cls.prod_description + ' ' + str(product_num),
                                   price=product_num)

    def test_get_view_with_correct_url_should_worK(self):
        resp = self.client.get('/products/')
        self.assertEqual(resp.status_code, 200)

