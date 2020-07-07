from django.urls import path
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
        path('', views.root_url),
        path('reg/', views.reg),
        path('signin/', views.sign_in),
        path('signout/', views.sign_out),

        path('about/', views.about),
        path('me/', views.me),
        path('addproduct/', views.add_product),
        path('products/', views.show_all_products),
        path('product/<int:idProduct>/', views.show_product),

]



