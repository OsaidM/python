#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('shows/<int:id>/edit', views.edit),
    path('edit_show/<int:id>', views.edit_show),
    path('shows/<int:id>', views.show),
    path('new', views.new),
    path('add_new', views.add_new),
    path('shows/<int:id>/delete', views.delete),
]
