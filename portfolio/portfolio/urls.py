from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include("about.urls")),
    url(r'^intro/', include("intro.urls")),
    url(r'^javapic/', include("javapic.urls")),
    url(r'^javapic_query/', include("javapic_query.urls")),
    url(r'^zen_mockup/', include("zen_mockup.urls")),
    url(r'^forum/', include('forum.urls')),

]
