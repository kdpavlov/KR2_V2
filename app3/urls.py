from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app3_home'),
    path('catalog/', views.catalog, name='app3_catalog'),
    path('catalog/<int:category_id>/', views.category_products, name='app3_category_products'),
    path('product/<int:product_id>/', views.product_detail, name='app3_product_detail'),
]

