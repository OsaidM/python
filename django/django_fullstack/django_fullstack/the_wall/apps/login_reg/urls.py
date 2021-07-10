from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^show$', views.show),
    url(r'^create/message$', views.message),
    url(r'^create/comment$', views.comment),
    url(r'^logout$', views.logout),
]