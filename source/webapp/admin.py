from django.contrib import admin
from .models import Product, Basket

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('pk', 'name', 'amount', 'price')
    list_display_links = ('pk', 'name')
    search_fields = ('name')


admin.site.register(Product)
admin.site.register(Basket)