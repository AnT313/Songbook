from django.shortcuts import render
from django.utils import timezone
from .models import Song

def song_list(request):
    songs = Song.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'songbook/song_list.html', {'songs': songs})
