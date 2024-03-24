from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review-list'),
    path('add/', views.add_review, name='add-review'),
]
