from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sa.views.home', name='home'),
    # url(r'^sa/', include('sa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^search/$','crontab.views.search',name='search'),
    url(r'^cron/$','crontab.views.cron',name='cron'),
    url(r'^help/$','crontab.views.help',name='help'),
#    url(r'^change_status/(\d+)/(.*)$','crontab.views.change_status'),
    url(r'^add/$','crontab.views.add'),
    url(r'^history/$','crontab.views.history_list'),
    url(r'^edit/(\d+)$','crontab.views.edit'),
    url(r'^$','crontab.views.login_views'),
    url(r'logout/$','crontab.views.logout_views',name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
