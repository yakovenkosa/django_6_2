from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterViews

app_name = 'users'

urlpatterns = [
    path('register/', RegisterViews.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="catalog:product_list"), name='logout'),
]