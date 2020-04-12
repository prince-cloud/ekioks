from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.productlist, name='product_list'),
    path('postad/', views.postad, name='postad'),
    path('edititem/<slug:product_slug>/', views.edititemview, name='edit_item'),
    path('<slug:category_slug>/', views.productlist, name='product_list_category'),
    path('detail/<slug:product_slug>/', views.productdetail, name='product_detail')
]  