from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from .services import get_products_by_category


class HomeView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_id = self.kwargs.get('pk')
        cache_key = f'product_{product_id}'

        product = cache.get(cache_key)
        if product is None:
            product = super().get_object(queryset)
            cache.set(cache_key, product, 60 * 15)  # 15 минут

        return product


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user != product.owner and not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_moderator = request.user.has_perm('catalog.delete_product')
        if request.user != product.owner and not is_moderator:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


def category_products(request, category_id):
    products = get_products_by_category(category_id)
    return render(request, 'products/category_products.html', {
        'products': products,
        'category_id': category_id,
    })
