from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('plus_two', views.plus_two),
    path('increment_by', views.increment_by),
]