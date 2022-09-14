from django.shortcuts import render
from play_cat.views.db import Cat


def index_view(request):
    return render(request, 'index.html')

cat = Cat()