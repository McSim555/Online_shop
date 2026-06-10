from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == "GET":
        return render(request, "home.html")


def contacts(request):
    if request.method == "GET":
        return render(request, "contacts.html")


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваша информация получена.")
    return render(request, "feedback.html")
