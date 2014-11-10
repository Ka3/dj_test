from django.conf.urls import patterns, include, url

from django.contrib import admin
from view_study.views import HelloTemplate

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello/$', 'view_study.views.hello'),
    #url(r'^hello/$', 'view_study.views.hello_legacy'),
    url(r'^hello/$', 'view_study.views.simple_hello'),
    url(r'^hello_class/$', HelloTemplate.as_view() ),
)

