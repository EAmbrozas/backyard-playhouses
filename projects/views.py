from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, ProjectImage
from .forms import ProjectForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            for file in request.FILES.getlist('images'):
                ProjectImage.objects.create(project=project, image=file)
            messages.success(request, 'Project added successfully.')
            return redirect('profile')
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})


def project_list(request):
    project_list = Project.objects.all().order_by('-date_posted')
    paginator = Paginator(project_list, 12)  # Show 12 projects per page.

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    return render(request, 'projects/project_list.html', {'projects': projects})

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully.')
            return redirect('profile')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/edit_project.html', {'form': form, 'project': project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully.')
        return redirect('profile')
    return render(request, 'projects/delete_project.html', {'project': project})