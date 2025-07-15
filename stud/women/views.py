from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the women index.")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

