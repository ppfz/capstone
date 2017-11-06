from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

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

# Create order page (Updated by Xie 11/6)
class OrderDetail(generic.ListView):
	#model = Order_Item
	paginate_by = 6
	context_object_name = 'Order_Details'   # your own name for the list as a template variable
	def get_queryset(self):
		return Order_Item.objects.select_related('Order_id').filter(Order_id__Res_id=self.request.user.username).filter(Status='CK')
	template_name = 'web/order_list.html'

# Updated the status of order_item in database and remove it from the screen - Xie 11/6
def statusUpdate(request, pk):
	if pk:
		Order_Item.objects.filter(pk=pk).update(Status='Delivered')
		return HttpResponseRedirect('/web/order')
