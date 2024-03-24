from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image_display']
    
    def image_display(self, obj):
        return obj.image.name
    image_display.short_description = 'Profile Image'

# Register the Profile model with the custom admin class
admin.site.register(Profile, ProfileAdmin)
