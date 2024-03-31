from django.shortcuts import render
from reviews.models import Review
from projects.models import Project

def homepage_view(request):
    latest_projects = Project.objects.all().order_by('-date_posted')[:6]
    latest_reviews = Review.objects.all().order_by('-date_posted')[:6]
    context = {
        'latest_projects': latest_projects,
        'latest_reviews': latest_reviews,
    }
    return render(request, 'home/index.html', context)
