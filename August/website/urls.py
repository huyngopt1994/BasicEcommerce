from django.conf.urls import url

from . import views

#create urlpatterns

urlpatterns =[
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about')
]