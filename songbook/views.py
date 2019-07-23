from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Song
from .forms import SongForm
from django.shortcuts import redirect

def song_list(request):
    songs = Song.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'songbook/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'songbook/song_detail.html', {'song': song})

def song_new(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.published_date = timezone.now()
            song.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'songbook/song_edit.html', {'form': form})

def song_edit(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.published_date = timezone.now()
            song.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'songbook/song_edit.html', {'form': form})