from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404

def hello(request):
	return HttpResponse("hello world")


def hello1(request,num):
	try:
		num= int(num)
	except ValueError:
		raise Http404()
