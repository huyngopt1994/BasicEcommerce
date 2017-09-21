from django.conf.urls  import include, url
from ajax.views import ColorList
from . import views
 
urlpatterns = [
    #Used as both the main page url, and for the search-form submission.
    #If the GET object exists, then the search-form is being submitted.
    #Otherwise, it's a normal page request.
    url(r"^$", ColorList.as_view(), name="color_list"),
 
    url(r"^like_color_(?P<color_id>\d+)/$", views.toggle_color_like, name="toggle_color_like"),
]