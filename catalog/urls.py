from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListViews, CatalogContactsView, ProductDetailViews
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', CatalogContactsView.as_view, name='contacts'),
    path('product_list/', ProductListViews.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/detail/', ProductDetailViews.as_view(), name='product_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
