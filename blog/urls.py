from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.top', name='top'),
    # url(r'^blog/', include('blog.foo.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^about/$', 'blog.views.about', name='about'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'logout.html'}),
)