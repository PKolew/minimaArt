from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from minima_art.picture_products.models import Order, Product, GalleryImage, Category, Review

from minima_art.picture_products.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'status', 'date_ordered', 'total_price')
    list_filter = ('status', 'date_ordered')
    search_fields = ('customer__username', 'product__name')
    ordering = ('-date_ordered',)
    readonly_fields = ('date_ordered', 'total_price')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available', 'category')
    list_filter = ('available', 'category')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.site_header = "Art Gallery Admin"
admin.site.site_title = "Gallery Admin Portal"
admin.site.index_title = "Welcome to the Art Gallery Management"
