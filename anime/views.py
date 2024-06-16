from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .forms import CommentForm, MovieForm
from .models import Movie, Category, Comment
from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                        password=password)
        user.save()

        # Send welcome message
        messages.success(request, 'Successfully registered You can Login.')

        return redirect('login')
    else:
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authenticated, log them in
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required
def profile(request):
    movies_list = Movie.objects.all()
    paginator = Paginator(movies_list, 12)  # Show 8 movies per page.

    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'profile.html', {'movies': movies})

@login_required
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movie_detail.html', context)


@login_required
def add_comment(request, pk):
    eachProduct = get_object_or_404(Movie, id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachProduct, commenter_name=name, comment_body=body, date_added=timezone.now())
            c.save()
            return redirect('movie_detail', pk=eachProduct.id)
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    context = {
        'form': form
    }

    return render(request, 'add_comment.html', context)


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)  # Retrieve comment by primary key
    product_id = comment.product.id  # Ensure the `product` attribute is correct

    if request.method == 'POST':
        comment.delete()
        return redirect(reverse('movie_detail', args=[product_id]))

    return render(request, 'delete_comment.html', {'comment': comment, 'product_id': product_id})


@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('profile')

