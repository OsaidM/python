from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('handle', views.handle),
]
