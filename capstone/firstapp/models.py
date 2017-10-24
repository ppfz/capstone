from django.db import models


# Create your models here.
class Product(models.Model):
#	product_id= models.IntegerField(max_length=11)
	product_name= models.CharField(max_length=100)
	description=models.CharField(max_length=255)
	price=models.IntegerField(max_length=11)
	res_id=models.IntegerField(max_length=11)
