from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListViews, CatalogContactsView, ProductDetailViews, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductByCategoryView, CategoryListView


app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', CatalogContactsView.as_view, name='contacts'),
    path('product_list/', ProductListViews.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/detail/', cache_page(60)(ProductDetailViews.as_view()), name='product_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path("category/<int:pk>/", ProductByCategoryView.as_view(), name="products_by_category"),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
]
