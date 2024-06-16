from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from anime.models import Movie
from .models import Cart, CartItem
from django.contrib import messages


def _cart_id(request):
    # Assuming you store the cart_id in session
    return request.session.get('cart_id')


def add_to_cart(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, movie=movie)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f'{movie.title}  already uploaded your cart.')
    else:
        messages.success(request, f'{movie.title} added to your cart.')

    # Redirect to movie_detail with a query parameter indicating if the item was newly added
    return redirect('movie_detail', pk=movie.id)


@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})


def cart_remove(request, movie_id):
    cart = Cart.objects.get(user=request.user)
    movie = get_object_or_404(Movie, id=movie_id)

    try:
        cart_item = CartItem.objects.get(movie=movie, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart:cart_detail')
