from django.conf.urls import include, url
from forum import views

urlpatterns = [
    url(r'^$', views.forum, name='forum'),
]