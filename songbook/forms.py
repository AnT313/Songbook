from django import forms
from .models import Song

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('title', 'song_author', 'song_details', 'text', 'chords')