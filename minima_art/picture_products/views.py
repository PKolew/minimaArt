from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Product, GalleryImage, Order
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, ReviewForm
from django.contrib.admin.views.decorators import staff_member_required
from minima_art.picture_products.forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'picture_products/product_list.html'
    context_object_name = 'products'

class GalleryListView(ListView):
    model = GalleryImage
    template_name = 'picture_products/gallery_image_list.html'
    context_object_name = 'images'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'picture_products/product_detail.html'
    context_object_name = 'product'

@login_required
def order_product(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Get the specific product
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.product = product  # Associate the specific product
            order.status = 'Pending'
            order.total_price = product.price  # Set the total price to the product price
            order.save()
            return redirect('picture_products:order_success')
    else:
        form = OrderForm()

    return render(request, 'forms/order.html', {'form': form, 'product': product})

def order_success(request):
    return render(request, 'picture_products/order_comleted.html')

@login_required
def my_orders(request):
    orders = Order.objects.filter(customer=request.user).order_by('-date_ordered')
    return render(request, 'picture_products/my_orders.html', {'orders': orders})


@staff_member_required
def manage_product(request, product_id=None):
    product = None
    if product_id:
        product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('picture_products:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'picture_products/manage_product.html', {'form': form})

@login_required
def submit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user
            review.product = product
            review.save()
            return redirect('picture_products:product_detail', pk=product.id)
    else:
        form = ReviewForm()

    return render(request, 'picture_products/submit_review.html', {'form': form, 'product': product})