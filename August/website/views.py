from django.shortcuts import render
from dao import get_9_best_seller, get_product
# Create your views here.

def home(request):
	name = "huy"
	objects = get_product(1)
	imagest_list = [object.link_image for object in objects]
	context = locals()
	template ='home.html'
	return render(request,template,context)

def about(request):
	number = 1
	objects = get_product(1)
	imagest_list = [object.link_image for object in objects]
	context = locals()

	template ='about.html'
	return render(request,template, context)

def test_ajax(request):
	context = locals()
	template = 'test_ajax.html'
	return render(request, template, context) 