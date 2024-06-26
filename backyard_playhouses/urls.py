from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('reviews/', include('reviews.urls')),
    path('profiles/', include('profiles.urls')),
    path('projects/', include(('projects.urls', 'projects'), namespace='projects')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
