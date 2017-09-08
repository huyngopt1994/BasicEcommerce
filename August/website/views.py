from django.shortcuts import render
from dao import get_9_best_seller
# Create your views here.

def home(request):
	name = "huy"
	#link_image = get_9_best_seller()
	context = locals()
	template ='home.html'
	return render(request,template,context)

def about(request):
	context = locals()
	template ='about.html'
	return render(request,template, context)