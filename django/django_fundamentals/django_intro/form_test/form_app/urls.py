#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('users', views.create_user),
    path('success', views.success),
]
