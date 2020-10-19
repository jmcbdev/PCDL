from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'browse/home.html, context')
