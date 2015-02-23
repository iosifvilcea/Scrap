from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'scrapyr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('scrapyr_app.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'scrapyr_app.views.login'),
    url(r'^home/$', 'scrapyr_app.views.home'),
    url(r'^logout/$', 'scrapyr_app.views.logout'),
]
