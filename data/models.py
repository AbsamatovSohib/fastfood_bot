from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=63, null=True, blank=True)
    last_name = models.CharField(max_length=63, null=True, blank=True)
    nick_name = models.CharField(max_length=63, null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.first_name


class Category(models.Model):
    title = models.CharField(max_length=63)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=63)

    price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} dan {self.amount} ta bor"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    amount = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args):
        self.total_price = self.product.price * self.amount
        self.total_price.save()

    def __str__(self):
        return f"{self.user.id} umumiy {self.total_price} so'mlik narsa sotib oldi"