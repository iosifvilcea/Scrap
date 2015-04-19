from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('scrapyr_app.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'scrapyr_app.views.login'),
    url(r'^logout/$', 'scrapyr_app.views.logout'),
    url(r'^profile/$', 'scrapyr_app.views.profile'),
    url(r'^edit/$', 'scrapyr_app.views.edit_profile'),
    url(r'^stock/(?P<ticker>[^\.]+)', 'scrapyr_app.views.view_stock', name='view_stock'),
    url(r'^article/(?P<slug>[^\.]+)', 'scrapyr_app.views.view_article', name='view_article'),
    url(r'^stocks/$', 'scrapyr_app.views.stocks'),
    url(r'^stock/$', 'scrapyr_app.views.stock'),
    url(r'^stockfeed/$', 'scrapyr_app.views.stockfeed'),
    url(r'^articles/$', 'scrapyr_app.views.articles'),
]
