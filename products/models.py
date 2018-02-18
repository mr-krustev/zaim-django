from django.db import models
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
        ('Accesories', (
                ('J', 'Jewelry'),
                ('S', 'Shoes'),
                ('B', 'Bags'),
        )),
    )

    product_type = models.CharField(max_length=3,
                                    choices=product_types)

    def save(self, *args, **kwargs):
        if self.product_type != "" and self.product_type not in self.product_types:
            raise ValidationError('Unknown product type selected.')
        super(Product, self).save(*args, **kwargs)

# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-choices
