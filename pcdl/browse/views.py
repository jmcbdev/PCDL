from django.shortcuts import render
from django.http import HttpResponse
from .models import Video


def index(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'browse/home.html', context)


def latest(request):
    return render(request, 'browse/latest.html', {'title': 'Latest'})

def videos(request):
    return render(request, 'browse/videos.html', {'title': 'Videos'})

def audios(request):
    return render(request, 'browse/audios.html', {'title': 'Audios'})