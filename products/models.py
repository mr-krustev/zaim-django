from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class Product(models.Model):
    # these three are a must I think, max_length can be adjusted
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)
    description = models.TextField(max_length=500)
    price = models.FloatField()

    # asked Yonca, she said there can be more than 1 of the same product
    quantity = models.IntegerField(default=0)

    # maybe useful for statistics, e.g. when was that product
    # last purchased/discounted/viewed
    last_modified = models.DateField(auto_now=True)

    product_types = (
        ('Clothes', (
                ('T', 'Tops'),
                ('B', 'Bottoms'),
                ('L', 'Lingerie'),
        )),
        ('Accessories', (
                ('J', 'Jewelry'),
                ('S', 'Shoes'),
                ('B', 'Bags'),
        )),
    )

    product_type = models.CharField(max_length=3,
                                    choices=product_types)

    def get_absolute_url(self):
        return reverse('detail', args=[self.product_id])

    def _is_valid_prod_type(self, pair):
        """Recursively check if product_type is a valid key in product_types."""
        has_found = False
        for key, value in pair:
            if isinstance(value, tuple):
                has_found = self._is_valid_prod_type(value)
            else:
                has_found = key == self.product_type

            if has_found:
                return has_found
        return has_found

    def save(self, *args, **kwargs):
        if self.product_type and not self._is_valid_prod_type(self.product_types):
            raise ValidationError('Unknown product type selected.')
        super(Product, self).save(*args, **kwargs)

# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-choices
