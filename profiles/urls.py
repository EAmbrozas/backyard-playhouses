from django.urls import path
from .views import profile_view, remove_profile_image  # Make sure to import your view function

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('remove-image/', remove_profile_image, name='profile-remove-image'),  # Add this line
]
