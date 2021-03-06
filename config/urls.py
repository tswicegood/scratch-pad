from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

# ADMIN_BASE is the base URL for your Armstrong admin.  It is highly
# recommended that you change this to a different URL unless you enforce a
# strict password-strength policy for your users.
ADMIN_BASE = "admin"


# Comment the next two lines out to disnable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foo.views.home', name='home'),
    # url(r'^foo/', include('foo.foo.urls')),

    # Comment the admin/doc line below to disable admin documentation:
    url(r'^%s/doc/' % ADMIN_BASE, include('django.contrib.admindocs.urls')),

    # Comment the next line to disable the admin:
    url(r'^%s/' % ADMIN_BASE, include(admin.site.urls)),

    # Load the Armstrong "success" page by default
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    url(r'^search/values/$', 'foo.views.values'),
    url(r'^search/facets/$', 'foo.views.facets'),
)
