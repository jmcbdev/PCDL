from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Video


def welcome(request):
    return render(request, 'browse/welcome.html')

@login_required    
def index(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'browse/home.html', context)

class VideoListView(ListView):
    model = Video
    template_name = 'browse/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'videos'
    ordering = ['date_posted']

class VideoDetailView(DetailView):
    model = Video

@login_required
def latest(request):
    context = {
        'videos': Video.objects.filter(latest=True)
    }
    return render(request, 'browse/latest.html', context)
@login_required
def videos(request):
    context = {
        'videos': Video.objects.filter(type_vid=True)
    }
    return render(request, 'browse/videos.html', context)

@login_required
def audios(request):
    context = {
        'videos': Video.objects.filter(type_vid=False)
    }
    return render(request, 'browse/audios.html', context)
