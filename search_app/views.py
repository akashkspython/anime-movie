from django.shortcuts import render
from anime.models import Movie
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.


def SearchResult(request):
    query = request.GET.get('q')
    movies = None
    if query:
        first_letter = query[0]
        movies = Movie.objects.filter(title__istartswith=first_letter)
        for letter in query[1:]:
            movies = movies.filter(title__icontains=letter)
    return render(request, 'search.html', {'query': query, 'movies': movies})