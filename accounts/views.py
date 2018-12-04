from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *

from .forms import SingUpForm, UpdateProfileForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SingUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def user_profile(request, id):
    user = get_object_or_404(User, id=id)
    profile = get_object_or_404(UserProfile, user=user)

    return render(request, 'profile/user_profile.html', {'profile': profile})


@login_required
def update_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', profile.user.id)
    else:
        form = UpdateProfileForm(instance=profile)
    return render(request, 'profile/update_profile.html', {'profile': profile, 'form': form})
