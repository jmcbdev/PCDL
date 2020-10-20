from django.shortcuts import render
from django.http import HttpResponse
from .models import Video


def index(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'browse/home.html', context)


def latest(request):
    context = {
        'videos': Video.objects.filter(latest=True)
    }
    return render(request, 'browse/latest.html', context)

def videos(request):
    context = {
        'videos': Video.objects.filter(type_vid=True)
    }
    return render(request, 'browse/audios.html', context)


def audios(request):
    context = {
        'videos': Video.objects.filter(type_vid=False)
    }
    return render(request, 'browse/audios.html', context)
