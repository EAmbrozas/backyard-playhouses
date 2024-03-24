from django import forms
from .models import Profile
from django.core.exceptions import ValidationError

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')

        # Check if an image has been uploaded
        if not image:
            raise ValidationError('Please select an image to upload.')

        return image
