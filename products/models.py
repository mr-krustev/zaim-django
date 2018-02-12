from django.db import models


class Product(models.Model):
    # these three are a must I think, max_length can be adjusted
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=False)
    description = models.CharField(max_length=500)
    price = models.FloatField(blank=False)
    
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

# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-choices
