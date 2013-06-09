from django.shortcuts import render_to_response,get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse,Http404
from django.template import Context,loader
from django.core.cache import get_cache
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import random

from hotels.models import Hotel,Location,Room,Client,Booked,Order

# Create your views here.
@requires_csrf_token
def index(request):
	context = {}
	context.update(csrf(request))
	return render_to_response('hotels/index.html',context)

@csrf_exempt
def searchHotel(request):
	key = request.POST['city']
	check_in_time = request.POST['checkin']
	check_out_time = request.POST['checkout']
	try:
		city_searched = Location.objects.get(city=key)
	except (KeyError, Location.DoesNotExist):
		city_list = Location.objects.all()
		print(city_list)
		if(len(city_list)>10):
			city_list_get = city_list[0:10]
		else:
			city_list_get = city_list
		context = Context({
			'city_list_get':city_list_get,
			'check_in_time':check_in_time,
			'check_out_time':check_out_time,
			})
		return render_to_response('hotels/recommendCity.html',context)
	else:
		hotel_list = Hotel.objects.filter(located_id=city_searched.id)
		context = Context({
			'hotel_list':hotel_list,
			'key':key,
			'check_in_time':check_in_time,
			'check_out_time':check_out_time,
			})
	return render_to_response('hotels/chooseHotel.html',context)

@csrf_exempt
def checkRoom(request,hotel_id):
	error = 0
	p = get_object_or_404(Hotel,pk=hotel_id)
	hotel = Hotel.objects.get(id=hotel_id)
	hotel_name = hotel.name
	hotel_star = hotel.star
	city_name = request.POST['city']
	check_in_time = request.POST['checkin']
	check_out_time = request.POST['checkout']
	context = Context({
			'error':error,
			'hotel_name':hotel_name,
			'hotel_star':hotel_star,
			'city_name':city_name,
			'check_in_time':check_in_time,
			'check_out_time':check_out_time,
		})
	return render_to_response('hotels/chooseRoomType.html', context)

@csrf_exempt
def confirm(request,hotel_id):
	p = get_object_or_404(Hotel,pk=hotel_id)
	error = 0
	hotel = Hotel.objects.get(id=hotel_id)
	hotel_name = hotel.name
	hotel_star = hotel.star
	city_name = request.POST['city']
	check_in_time = request.POST['checkin']
	check_out_time = request.POST['checkout']
	room_total = request.POST['roomTotal']
	all_num = [[] for i in range(1,int(room_total)+1)]
	adults_num = []
	children_num = []
	number_get = []
	price_get = []
	room_id_get = []
	price_all = 0
	j_set = [0 for i in range(1,int(room_total)+1)]
	try:
		for i in range(1,int(room_total)+1):
			adults_num = request.POST['room_'+str(i)+'_adults']
			all_num[i-1].append(adults_num)
			children_num = request.POST['room_'+str(i)+'_children']
			all_num[i-1].append(children_num)
			room = Room.objects.filter(adult=adults_num,children=children_num,belongto_id=hotel_id)
			number_get = room[j_set[i-1]].roomNumber
			if(i>=2):
				print(all_num[i-2])
				for a in all_num[0:i-1]:
					if (number_get == a[2]):
						j_set[i-1] += 1
						number_get = room[j_set[i-1]].roomNumber
			room_id_get.append(room[j_set[i-1]].id)
			all_num[i-1].append(number_get)
			price_get = room[j_set[i-1]].price
			price_all += price_get
			all_num[i-1].append(price_get)

	except IndexError:
		error = 1
		print(error)
		context = Context({
			'error':error,
			'hotel_name':hotel_name,
			'hotel_star':hotel_star,
			'city_name':city_name,
			'check_in_time':check_in_time,
			'check_out_time':check_out_time,
		})
		return render_to_response('hotels/chooseRoomType.html',context)
	except ValueError:
		error = 1
		context = Context({
			'error':error,
			'hotel_name':hotel_name,
			'hotel_star':hotel_star,
			'city_name':city_name,
			'check_in_time':check_in_time,
			'check_out_time':check_out_time,
		})
		return render_to_response('hotels/chooseRoomType.html',context)
	context = Context({
		'hotel_name':hotel_name,
		'hotel_star':hotel_star,
		'city_name':city_name,
		'check_in_time':check_in_time,
		'check_out_time':check_out_time,
		'all_num':all_num,
		'price_all':price_all,
		'room_id_get':room_id_get
	})
	return render_to_response('hotels/confirmReservation.html',context)

@csrf_exempt
def success(request,hotel_id):
	p = get_object_or_404(Hotel,pk=hotel_id)

	price_all = request.POST['price_all']
	check_in_time = request.POST['checkin']
	check_out_time = request.POST['checkout']
	client_firstname = request.POST['firstname']
	client_lastname = request.POST['lastname']
	client_require = request.POST['requirement']
	client_smoking = request.POST['smoking']

	client = Client(smoking=client_smoking,firstname=client_firstname,lastname=client_lastname,requirement=client_require)
	client.save()

	client_id = client.id
	order_code = str(random.randint(10000000,99999999))
	order = Order(checkin=check_in_time,checkout=check_out_time,total=price_all,date=timezone.now(),client_id=client_id,code=order_code)
	order.save()
	order_id = order.id
	num_all = request.POST['room_all']
	s = num_all[1:(len(num_all)-2)]
	order_id_set = s.split('L,')
	for i in range(0,len(order_id_set)):
		booked = Booked(room_id=int(order_id_set[i]),order_id=order_id)
		booked.save()
	context = Context({
			'order_code':order_code,
		})
	return render_to_response('hotels/success.html',context)

@csrf_exempt
def sortHotels(request, by):
	key = request.POST['city']
	check_in_time = request.POST['checkin']
	check_out_time = request.POST['checkout']
	city_searched = Location.objects.get(city=key)
	print check_out_time
	if(by =="star"):
		hotel_list = Hotel.objects.filter(located_id=city_searched.id).order_by("-star")
	elif(by == "name"):
		hotel_list = Hotel.objects.filter(located_id=city_searched.id).order_by("name")
	return render_to_response('hotels/getHotelList.html', locals())




