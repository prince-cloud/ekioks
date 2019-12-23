from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.productlist, name='product_list'),
    path('sellitem/', views.sellitemview, name='sell_item'),
    path('edititem/<slug:product_slug>/', views.edititemview, name='edit_item'),
    path('<slug:category_slug>/', views.productlist, name='product_list_category'),
    path('detail/<slug:product_slug>/', views.productdetail, name='product_detail')
]  