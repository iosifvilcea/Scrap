from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'scrapyr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^scrapyr_app/', include('userena.urls')),
    url(r'^$', include('scrapyr_app.urls')),
    url(r'^scrapyr_app/signup/$', 'userena.views.signup')
]
