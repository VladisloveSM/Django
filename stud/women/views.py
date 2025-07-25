from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    { 'id': 1, 'title': 'Angelina Golie', 'content': 'Biography of Angelina Golie', 'is_published': True },
    { 'id': 2, 'title': 'Jennifer Aniston', 'content': 'Biography of Jennifer Aniston', 'is_published': True },
    { 'id': 3, 'title': 'Scarlett Johansson', 'content': 'Biography of Scarlett Johansson', 'is_published': False },
]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Create your views here.

def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', data)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_slug}</p>")

def archive(request, year):
    if year > 2025:
        uri = reverse('cats', args=('sport',))
        return HttpResponseRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

