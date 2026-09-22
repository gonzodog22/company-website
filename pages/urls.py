from django.urls import path

from .views import home_page_view, AboutPageView, products_page_view

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", home_page_view, name="home"),
    path("products/", products_page_view.as_view(), name="products"),
]