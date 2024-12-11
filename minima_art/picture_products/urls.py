from django.urls import path
from .views import ProductListView, GalleryListView, ProductDetailView, order_product, order_success, my_orders, \
    manage_product, submit_review
from minima_art.web import views as web_views

app_name = 'picture_products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Gallery
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/index.html', web_views.home, name='home'),

    # Orders
    path('<int:pk>/order/', order_product, name='order_product'),
    path('order-success/', order_success, name='order_success'),
    path('my-orders/', my_orders, name='my_orders'),
    path('<int:product_id>/review/', submit_review, name='submit_review'),

    # Product Management
    path('manage_product/', manage_product, name='manage_product'),
    path('manage_product/<int:product_id>/', manage_product, name='edit_product'),

]
