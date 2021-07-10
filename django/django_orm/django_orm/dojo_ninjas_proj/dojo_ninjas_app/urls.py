#from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.root),
    path('add/dojo', views.addDojo),
    path('add/ninja', views.addNinja)
]
