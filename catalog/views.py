from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request
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
from .forms import ProductForm, ProductModeratorForm
from .services import get_products_list_from_cache


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


    def get_queryset(self):
        user = self.request.user
        qs = get_products_list_from_cache()
        if user.has_perm("catalog.can_unpublish_product"):
            return qs
        return qs.filter(is_published=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse("catalog:product_detail", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.delete_product") and user.has_perm(
            "can_unpublish_product"
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = "catalog.delete_product"
    template_name = "product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:product_list")

    def has_permission(self):
        user = self.request.user
        product = self.get_object()
        if user == product.owner:
            return True
        if user.has_perm("catalog.delete_product"):
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductPublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "catalog.can_unpublish_product"
    raise_exception = True

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = not product.is_published
        product.save()
        return redirect(
            request.META.get("HTTP_REFERER", reverse("catalog:product_list"))
        )
