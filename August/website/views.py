from django.shortcuts import render,render_to_response
from dao import get_9_best_seller, get_product
from .models import product
# Create your views here.

from django.views.generic import ListView

class HomeList (ListView):
	"""
	Displays all colors in a table with only two columns: color , and a "like/unlike" button.
	"""

	model = product  #  It mean query table color alls
	# template variable to access model in template
	context_object_name = "product"

	def get_template_names(self):
		return ['home.html']

	def dispatch(self, request, *args, **kwargs):
		self.request = request #So get_context_data can access it.
		return super(HomeList, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		"""
		Returns the all colors, for display in the main table. The search result query set, if any,  is passed as context.
		"""
		#Query all color objects
		return super(HomeList, self).get_queryset()

	def get_context_data(self, **kwargs):
		#Pass additional context variables to the template
		#firt thing get the current object 
		context = super(HomeList, self).get_context_data(**kwargs)
		objects = get_product(1)
		image_list = [object.link_image for object in objects]
		context['image_list'] = image_list
		return context


def change_product(request, product_id):

	objects = get_product(product_id)
	image_list = [object.link_image for object in objects]

	return render(request, "render_product.html", {"image_list":image_list})