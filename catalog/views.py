from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    TemplateView,
    DeleteView,
    UpdateView,
)
from catalog.models import Product, Contact
from .forms import ProductForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        latest_products = Product.objects.order_by("created_at")[:5]
        for product in latest_products:
            print(
                f"Продукт: {product.name}, Цена: {product.price}, Дата создания: {product.created_at}"
            )
        return render(request, "home.html", {"latest_products": latest_products})


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            contact_shown = Contact.objects.get(name="Филиал 1")
        except Contact.DoesNotExist:
            contact_shown = None
        except Contact.MultipleObjectsReturned:
            contact_shown = Contact.objects.filter(name="Филиал 1").first()
        context["contact"] = contact_shown
        return context


class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "feedback.html")

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваша информация получена.")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:product_list")
