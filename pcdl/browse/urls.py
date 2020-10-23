from django.urls import path
from .views import VideoListView, VideoDetailView
from . import views


urlpatterns = [
    # path('browse/', views.index, name='browse-home'),
    path('', VideoListView.as_view(), name='browse-home'),
    path('video/<int:pk>', VideoDetailView.as_view(), name='video-detail'),
    path('latest/', views.latest, name='browse-latest'),
    path('videos/', views.videos, name='browse-videos'),
    path('audios/', views.audios, name='browse-audios'),
]