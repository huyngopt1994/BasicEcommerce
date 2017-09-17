# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 
from django.views.generic import ListView
from ajax.models import Color

MIN_SEARCH_CHARS = 2
"""
The minimum number of characters required in a search. If there are less,the form submission is ignored. This value is used by the below view and the template.
"""
# Create your views here.

class ColorList (ListView):
	"""
	Displays all colors in a table with only two columns: color , and a "like/unlike" button.
	"""

	model = Color 
	context_object_name = "colors"

	def dispatch(self, request, *args, **kwargs):
		self.request = request #So get_context_data can access it
		return super(ColorList, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		"""
		Returns the all colors, for display in the main table. The search result query set, if any,  is passed as context.
		"""
		return super(ColorList, self).get_queryset()

	def get_context_data(self, **kwargs):
		#The current context
		context = super(ColorList, self).get_context_data(**kwargs)
		global MIN_SEARCH_CHARS

		search_text = " " #Assume no search
		if (self.request.method == "GET"):
			search_text = self.request.GET.get("search_text", "").strip().lower()
			if(len(search_text) < MIN_SEARCH_CHARS):
				search_text = "" #Ignore search

		if (search_text != ""):
			color_search_results = Color.objects.filter(name = search_text)
		else :
			#An empty list instead of None. In the template , use {% if color_search_results.count >0 %}
			color_search_results = []

		# Add items to the context :
		# The search text for display and result set
		context["search_text"] = search_text
		context["color_search_results"]  = color_search_results

		# For display under search form 
		context["MIN_SEARCH_CHARS"] = MIN_SEARCH_CHARS

		return context

	def toggle_color_like(request, color_id):
		"""Toggle "like" for a single color, then refresh the color-list page."""
    	color = None
    	try :
    		#get color by color_id 
    		color = Color.objects.query(id=color_id)
    	except Color.DoesNotExist as e 
    		raise ValueError("Unknown color.id =" +  str(color.id)+ "Original error:" + str(e))

    	color.is_favorited = not color.is_favorited

    	color.save() # Commit the change of database
    	return redirect("color_list")


