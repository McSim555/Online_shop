from django.urls import path
from catalog.apps import CatalogConfig
from . import views
from .views import ProductDetailView, ProductListView, ProductCreateView, ContactsView, HomeView, FeedbackView

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("main/", ProductListView.as_view(), name="product_list"),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
]
