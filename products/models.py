from django.contrib import auth
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=25, decimal_places=2, default=99.99)

    class Meta:
        db_table = 'Product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    @property
    def sale_price(self):
        return '%.2f' % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"
