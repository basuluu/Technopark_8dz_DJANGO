from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<id>\d+)/(?P<page>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post_new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^search/$', views.search_form, name='search_form'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'dairy/login.html'), name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile')
    ]
