from django.urls import path

from . import views
from .views import *
urlpatterns=[
    path('',views.fun,name='home'),
    path('<slug:c_slug>/', views.fun, name='prod_brand'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodDetails, name='details'),
    path('search',views.searching,name='search'),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout")

]