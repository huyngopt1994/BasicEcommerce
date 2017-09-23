from django.shortcuts import render
from dao import get_9_best_seller, get_product
# Create your views here.

def home(request):
	name = "huy"
	objects = get_product(1)
	image_list = [object.link_image for object in objects]
	context = locals()
	template ='home.html'
	return render(request,template,context)

def about(request):
	number = 1
	objects = get_product(1)
	image_list = [object.link_image for object in objects]
	context = locals()

	template ='about.html'
	return render(request,template, context)

def change_product(request, product_id):
	objects=get_product(product_id)
	image_list = [object.link_image for object in objects]

	return render(request, "ajax/color_like_link_to_html.txt", {"image_list":image_list})