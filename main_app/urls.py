from django.urls import path
from . import views # Import views from the current app


urlpatterns = [
    # our routes for the main_app
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('gallery/', views.gallery, name='gallery'),  # Gallery page (using home view as placeholder)
    
]

