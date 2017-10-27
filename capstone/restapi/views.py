from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse,StreamingHttpResponse,JsonResponse
from web.models import *
from restapi.serializers import*
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

'''
class JSONResponse(StreamingHttpResponse):
	def __init__(self, data, **kwargs):
		content= JSONRenderer().render(data)
		kwargs['content_type']='application/json'
		super(JsonResponse, self).__init__(content,**kwargs)
'''
def menu_item(request, str):
	if request.method == 'GET':
                items =Menu_Item.objects.filter(Menu_id_id=str)
                ser = MenuItemSerializer(items,many=True)
                return JsonResponse(ser.data,safe=False)



def menu_list(request,str):

	if request.method == 'GET':
		menus =Menu.objects.filter(Res_id_id=str)
		ser = MenuSerializer(menus, many=True)
		return JsonResponse(ser.data,safe=False)
	'''
	elif request.method == 'POST':
		data = JSONParser().parse(request)
        	serializer = MenuSerializer(data=data)
        	if serializer.is_valid():
	            	serializer.save()
          
  		return JsonResponse(serializer.data, status=201)

        	return JsonResponse(serializer.errors, status=400)
	'''

