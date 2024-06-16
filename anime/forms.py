from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'actors', 'release_date', 'category', 'youtube_trailer_link']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),

        }
