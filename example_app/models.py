from django.db import models


class Order(models.Model):
    customer = models.IntegerField()

    @property
    def total_price(self):
        return sum([
            o.product.price * o.quantity
            for o in self.ordered_products.select_related('product').all()
        ])


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, related_name='ordered_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
