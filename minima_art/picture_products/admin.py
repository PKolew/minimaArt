from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Product, Category, Tag, GalleryImage, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description')
    ordering = ('name',)
    prepopulated_fields = {"name": ("category",)}
    readonly_fields = ('id',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'rating', 'comment',)
    list_filter = ('rating',)
    search_fields = ('product__name', 'customer__username', 'comment')

    def product_link(self, obj):
        """Link to the product page in admin."""
        url = reverse('admin:picture_products_product_change', args=[obj.product.id])
        return format_html('<a href="{}">{}</a>', url, obj.product.name)

    product_link.short_description = "Product"

    def customer_link(self, obj):
        """Link to the customer page in admin."""
        url = reverse('admin:auth_user_change', args=[obj.customer.id])
        return format_html('<a href="{}">{}</a>', url, obj.customer.username)

    customer_link.short_description = "Customer"