from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Contact


def home(request):
    latest_products = Product.objects.order_by('created_at')[:5]
    for product in latest_products:
        print(f"Продукт: {product.name}, Цена: {product.price}, Дата создания: {product.created_at}")

    if request.method == "GET":
        return render(request, "home.html")


def contacts(request):
    if request.method == "GET":
        try:
            contact_shown = Contact.objects.get(name='Филиал 1')
        except Contact.DoesNotExist:
            contact_shown = None
        except Contact.MultipleObjectsReturned:
            contact_shown = Contact.objects.filter(name='Филиал 1').first()
        return render(request, "contacts.html", {'contact': contact_shown})


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваша информация получена.")
    return render(request, "feedback.html")
