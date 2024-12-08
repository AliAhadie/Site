from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):

    return HttpResponse("<h1> home page </h1>")

def about_view(request):
    return HttpResponse ('<h1> about page</h1>')

def content_view(request):
    return HttpResponse('<h1> content page</h1>')
