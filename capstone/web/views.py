from django.shortcuts import render

# Create your views here.

from .models import Beacon, Menu, Menu_Item, Order, Order_Item, Payment, Restaurant, Product
from django.views import generic

# Create index page
def index(request):
	"""
	View function for home page of site.
	"""
	num_restaurants=Restaurant.objects.all().count()
	
	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'num_restaurants':num_restaurants},
    )


# Create order page	
class OrderDetail(generic.ListView):
	#model = Order_Item
	context_object_name = 'Order_Details'   # your own name for the list as a template variable
	queryset = Order_Item.objects.select_related('Order_id')
	template_name = 'web/order_list.html'

