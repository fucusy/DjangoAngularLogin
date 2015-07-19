__author__ = 'fucus'
from django.conf.urls import url
from session_auth import views

urlpatterns = [
    url(r'^session_auth/(?P<username>[A-Za-z0-9_]+)/(?P<password>.+)/$', views.login),
    url(r'^profile',views.get_profile),
    url(r'^logout',views.logout),
]
