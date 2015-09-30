from django.conf.urls import include, url
from javapic_query import views

urlpatterns = [
    url(r'^$', views.javapic_query, name='javapic_query'),
    url(r'^query_join', views.query_join, name='join'),
    url(r'^query_gallery', views.query_gallery, name='gallery'),
]