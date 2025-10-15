from django.urls import path
from . import views # Import views from the current app


urlpatterns = [
    # our routes for the main_app
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('gallery/', views.gallery, name='gallery'),  # Gallery page (using home view as placeholder)
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),  # Car detail page
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),

]

