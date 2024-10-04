from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListViews, CatalogContactsView, ProductDetailViews

app_name = CatalogConfig.name

urlpatterns = [
    path('product_list/', ProductListViews.as_view(), name='product_list'),
    path('contacts/', CatalogContactsView.as_view, name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailViews.as_view(), name='product_detail'),
]
