from django.conf.urls import patterns, include, url

urlpatterns = patterns('posts.views',
    url(r'^detail/(?P<id>.*)/', 'detail', name='detail'),
    url(r'^entry/$', 'add_entry', name='add_entry'),
    url(r'^edit/(?P<id>.*)/$', 'edit_entry', name='edit_entry'),
    url(r'^delete/(?P<id>.*)/$', 'delete_entry', name='delete_entry'),
    # url(r'^blog/', include('blog.foo.urls')),

)
