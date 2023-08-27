from django.contrib import admin
from .models import Customer, Cart, Product, People

admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(People)