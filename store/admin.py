from django.contrib import admin

from store.models.customer import Customer
from .models.product import Product
from .models.categories import Category
from .models.customer import Customer
from .models.orders import Order
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdiminCategory(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdiminCategory)
admin.site.register(Customer)
admin.site.register(Order)