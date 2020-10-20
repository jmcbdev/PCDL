from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='browse-home'),
    path('latest/', views.latest, name='browse-latest'),
    path('videos/', views.videos, name='browse-videos'),
    path('audios/', views.audios, name='browse-audios'),
]