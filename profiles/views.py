from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib import messages
from reviews.models import Review


@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile image has been updated.')
            return redirect('profile')
        else:
            messages.warning(request, 'Please select an image to upload.')
    else:
        p_form = ProfileUpdateForm(instance=profile)

    reviews = Review.objects.all().order_by('-date_posted')[:6]
    
    context = {'p_form': p_form, 'reviews': reviews}
    return render(request, 'profiles/profile.html', context)

@login_required
def remove_profile_image(request):
    profile = request.user.profile

    if profile.image:
        profile.image.delete()
        profile.image = None
        profile.save()
        messages.success(request, 'Your profile image has been removed.')
    else:
        messages.info(request, 'No custom profile image to remove.')

    return redirect('profile')
