from django.urls import path
from catalog.apps import CatalogConfig
from .views import (
    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ContactsView,
    HomeView,
    FeedbackView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("main/", ProductListView.as_view(), name="product_list"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
