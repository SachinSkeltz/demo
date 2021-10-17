from django.urls import path
from . import views

urlpatterns = [
    path('about',views.about,name="about"),
    path('gallery',views.gallery,name="gallery"),
    path('contact',views.contact,name="contact"),
    path('products',views.products,name="products"),
    path('home',views.home,name="home"),

    ]