from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'analysis.views.home', name='home'),
    url(r'^about.html', 'analysis.views.about', name='about'),
    url(r'^mapanalysis.html', 'analysis.views.map', name='map'),
    url(r'^chartanalysis.html', 'analysis.views.chart', name='chart'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
