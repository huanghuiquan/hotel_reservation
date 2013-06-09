from django.conf.urls import patterns,url
from hotels import views


urlpatterns = patterns('',

	url(r'^index/$',views.index,name='index'),

	url(r'^index/searchHotel/$',views.searchHotel,name='searchHotel'),

	url(r'^index/(?P<hotel_id>\d+)/checkRoom/$',views.checkRoom,name='checkRoom'),

	url(r'^index/(?P<hotel_id>\d+)/confirm/$',views.confirm,name='confirm'),

	url(r'^index/(?P<hotel_id>\d+)/success/$',views.success,name='success'),

    url(r'^index/searchHotel/sortHotels/(?P<by>\w+)$',views.sortHotels,name='sortHotels'),
)