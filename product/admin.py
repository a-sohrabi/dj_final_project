from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Category, Product
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)


class MyAdminSite(AdminSite):

    site_title = 'Navan nuts Admin'

    site_header = 'Administration'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('price', 'category', )
    list_editable = ('price',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


