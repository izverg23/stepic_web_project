from django.conf.urls import patterns, include, url

urlpatterns = patterns('qa.views',
	url(r'^$', 'index', name='index'),
	url(r'^login/', 'login', name='login'),
	url(r'^signup/', 'signup', name='signup'),
	url(r'^question/(?P<quest_id>[0-9]+)/$', 'question', name='question'),
	url(r'^ask/', 'ask', name='ask'),
	url(r'^answer/', 'answer', name='answer'),
	url(r'^popular/', 'popular', name='popular'),	
	url(r'^new/', 'test', name='new'),	
)
