

# Create your views here.
# TuneTracker/views.py

# TuneTracker/views.py

from django.shortcuts import render, redirect
from .models import Song,Artist
from .forms import SongForm,ArtistForm


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = Song.objects.get(pk=pk)
    return render(request, 'song_detail.html', {'song': song})

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()

    return render(request, 'add_artist.html', {'form': form})

def artist_list(request):
    artists = Artist.objects.all()
    artist_data = []

    for artist in artists:
        song_count = artist.song_set.count()
        artist_data.append({'artist': artist, 'song_count': song_count})

    return render(request, 'artist_list.html', {'artists': artist_data})