
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from web.models import *
from restapi.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
@csrf_exempt
# Given a beacon id we find the resturant, then return all avaliable menus for this resturant.
def menu_list2(request):
    if request.method == 'POST':
        val = request.data['beacon']
        res_id = Beacon.objects.get(Beacon_id=val).Res_id
        menus = Menu.objects.filter(Res_id_id=res_id)
        ser = MenuSerializer(menus, many=True)
        return JsonResponse(ser.data, safe=False)


@api_view(['GET', 'POST'])
@csrf_exempt
# Given a order id we update the payment info after a payment in conducted
def pay(request):
    if request.method == 'POST':
        if Payment.objects.filter(Order_id=request.data['Order_id']).exists():
            return Response("You have paid the order already", status=status.HTTP_200_OK)
        ser = PaymentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@csrf_exempt 
def order_item(request):
    if request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
@csrf_exempt
def new_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
def new_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
		 # create an entry in Payment table
          #  order_id = serializer.data.get['Order_id']
            ser = PaymentSerializer(data=serializer.data)
            if ser.is_valid():
                ser.save()
	    return Response(serializer.data, status=status.HTTP_200_OK)
#            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
def get_res_info(request, str):
    if request.method == 'GET':
        info = Restaurant.objects.get(Res_id=str)
        ser = ResSerializer(info)
        return JsonResponse(ser.data, safe=False)


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
