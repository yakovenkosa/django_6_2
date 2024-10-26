from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from catalog.forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.services import get_product_from_cache, get_products_by_category


class ProductListViews(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return get_product_from_cache()


class ProductDetailViews(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class CatalogContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductByCategoryView(View):
    model = Category

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        products = get_products_by_category(pk)

        return render(request, 'catalog/category_products.html', {'category': category, 'products': products})

class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categorys"
