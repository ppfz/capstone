from web.models import *
from django_rest_framework import serializers

class MenuSerializer(serializers.Serializer):
	menu_type= serializers.CharField(max_length=100)
#	res_name= serializers.CharField(max_length=100)
	
	def restore_object(self, attrs, instance=None):
		if instance:
			instance.menu_type=attrs['menu_type']
	#		instance.res_name= attrs['res_name']
#			instance.author= attrs[]
			return instance
	#	return Menu(**attrs)
