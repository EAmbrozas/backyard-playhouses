from django import forms
from .models import Project
from django_summernote.widgets import SummernoteWidget

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']
        widgets = {
            'description': SummernoteWidget(),
        }
