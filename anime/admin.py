# movies/admin.py

from django.contrib import admin
from .models import Movie, Category,Comment

admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Comment)