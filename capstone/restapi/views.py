
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from web.models import *
from restapi.serializers import *
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



def menu_list(request, str):
    if request.method == 'GET':
        menus = Menu.objects.filter(Res_id_id=str)
        ser = MenuSerializer(menus, many=True)
        return JsonResponse(ser.data, safe=False)

def menu_item(request, str):
    if request.method == 'GET':
        items = Product.objects.filter(menu_item__Menu_id=str)
        ser = MenuItemSerializer(items, many=True)
        return JsonResponse(ser.data, safe=False)
