from . import views
from django.urls import path

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('show/', views.show),
    path('product/', views.product),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.change)
]