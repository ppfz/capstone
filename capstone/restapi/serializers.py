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
    Price = serializers.DecimalField(decimal_places=2, max_digits=10,coerce_to_string=False)
    Description = serializers.CharField(max_length=500)

#    def create(self, validated_data):
#	return Product.objects.create(**validated_data)
	


class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model=Menu
		fields = ('Type','Menu_id','Res_id','Res_id_id')
