from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, 'main/index.html')


def login(request):
    return render(request, 'main/login.html')


def sign_up(request):
    pass


def book(request, bookid):
    pass


def page_not_found(request, exeption):
    return HttpResponseNotFound('<h1> Page Not Found </h1>')
