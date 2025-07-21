from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'women/index.html', data)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

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

