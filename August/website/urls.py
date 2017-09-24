from django.conf.urls import url
from .views import HomeList
from . import views

# create urlpatterns

urlpatterns = [
    url(r'^$', HomeList.as_view(), name='home'),
    url(r"^change_product_(?P<product_id>\d+)/$", views.change_product, name='change_product'),

]
