from django.urls import path
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
        path('', views.RootUrl),
        path('reg/', views.Reg),
        path('signin/', views.SignIn),
        path('signout/', views.SignOut),

        path('about/', views.About),
        path('me/', views.Me),
        path('addproduct/', views.AddProduct),
        path('products/', views.ShowAllProducts),
        path('product/<int:idProduct>/', views.ShowProduct),

]



