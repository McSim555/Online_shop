from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("feedback/", views.feedback, name="feedback"),
    path("product/<int:pk>/", views.product_info, name="product_info"),
    path("main/", views.products_info, name="products_info"),
]
