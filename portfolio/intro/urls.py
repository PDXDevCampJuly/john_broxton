from django.conf.urls import include, url
from intro import views

urlpatterns = [
    url(r'^$', views.intro, name='intro'),
]