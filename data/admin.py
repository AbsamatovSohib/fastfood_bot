from django.contrib import admin
from data.models import User, Product, Category, Order

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
