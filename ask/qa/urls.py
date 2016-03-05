from django.conf.urls import patterns, include, url

urlpatterns = patterns('qa.views',
	#url(r'^', 'test', name='index'),
	url(r'^login/$', 'test', name='login'),
	url(r'^signup/$', 'test', name='signup'),
	url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),
	url(r'^ask/$', include("ask.urls")),
	url(r'^popular/$', 'test', name='popular'),	
	url(r'^new/$', 'test', name='new'),	
)