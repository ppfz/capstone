from restapi.models import *
from web.models import *
from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    '''
        class Meta:

                model=Product
                fields = ('Product_id','Product_name','Price','Description')
    '''

    Product_id = serializers.CharField(max_length=200)
    Product_name = serializers.CharField(max_length=200)
    Price = serializers.FloatField(max_value=None, min_value=None)
    Description = serializers.CharField(max_length=500)

#    def create(self, validated_data):
#	return Product.objects.create(**validated_data)
	
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = ('Product_id', 'Product_id_id', 'Order_id_id', 'Order_id', 'Quantity')

class ResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('__all__')



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')

class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model=Menu
		fields = ('Type','Menu_id','Res_id','Res_id_id')
