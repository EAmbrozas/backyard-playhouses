from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

def review_list(request):
    reviews_list = Review.objects.all().order_by('-date_posted')
    paginator = Paginator(reviews_list, 12)  # Show 12 reviews per page.

    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)

    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully.')
            # Get the next URL from the request. If none is provided, default to 'profile'.
            next_url = request.GET.get('next', reverse('profile'))
            return HttpResponseRedirect(next_url)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form, 'next': request.GET.get('next', '')})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully.')
        # Get the "next" URL from the form data. If it's not provided, default to the review list.
        next_url = request.POST.get('next', reverse('review_list'))
        return HttpResponseRedirect(next_url)
    else:
        # If it's a GET request, just render the confirmation page
        return render(request, 'reviews/delete_review.html', {'review': review})