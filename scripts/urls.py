from django.conf.urls import patterns, url

from scripts import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<script_id>\d+)/write_review/$', views.write_review, name='write_review'),
)
