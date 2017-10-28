from restapi.models import *
from web.models import *
from rest_framework import serializers



class MenuItemSerializer(serializers.ModelSerializer):
	class Meta:
#		model=Menu_Item
#		fields = ('Menu_id','Menu_id_id','Product_id','Product_id_id')
		model=Product
		fields = ('Product_id','Product_name','Price','Description')



class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model=Menu
		fields = ('Type','Menu_id','Res_id','Res_id_id')

#	Type= serializers.CharField(max_length=100)
#	Menu_id= serializers.CharField(max_length=100)
	
#	def restore_object(self, attrs, instance=None):
#		if instance:
#			instance.Type=attrs['Type']
#			instance.Menu_id=attrs['Menu_id']
	#		instance.res_name= attrs['res_name']
#			instance.author= attrs[]
#			return instance
	#	return Menu(**attrs)
