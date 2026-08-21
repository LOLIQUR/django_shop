from django.urls import path
from .views import HomeView, ProductDetailView, ContactsView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
