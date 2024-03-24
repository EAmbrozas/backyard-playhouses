from django.shortcuts import render
from reviews.models import Review

def homepage_view(request):
    # Fetch the latest 3 reviews
    latest_reviews = Review.objects.all().order_by('-date_posted')[:6]
    return render(request, 'home/index.html', {'latest_reviews': latest_reviews})