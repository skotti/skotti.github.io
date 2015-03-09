from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'polls/login.html'
    }, name='login'),
    url(r'^post_show/$', views.post_show, name='post_show'),
    url(r'^logout/$', views.logout_view,  name='logout'),

 )