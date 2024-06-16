from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def account_view(request):
    return render(request, 'account.html')


@login_required
def profile(request):
    return render(request, 'account.html')
