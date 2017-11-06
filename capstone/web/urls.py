from django.conf.urls import url

from . import views

#mapping for web pages
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^order/$', views.OrderDetail.as_view(), name='order'),
	# redirect after updating status - Xie 11/6
	url(r'^(?P<pk>\d+)/$', views.statusUpdate, name='status'),
]
