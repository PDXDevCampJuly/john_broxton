from django.conf.urls import include, url
from javapic import views

urlpatterns = [
    url(r'^$', views.javapic, name='javapic'),
    url(r'^join', views.join, name='join'),
    url(r'^gallery', views.gallery, name='gallery'),
]