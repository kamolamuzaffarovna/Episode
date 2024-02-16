from django.urls import path

from .views import EpisodeListView, EpisodeDetailView, EpisodePlaylist

app_name = 'episode'

urlpatterns = [
    path('list/', EpisodeListView.as_view(), name='list'),
    path('detail/', EpisodeDetailView.as_view(), name='detail'),
    path('music/', EpisodePlaylist.as_view(), name='playlist')
]