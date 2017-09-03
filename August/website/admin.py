from django.contrib import admin

from .models import (type,
											product,
											order,
											user)

# Register your models here.

admin.site.register(type)
admin.site.register(product)
admin.site.register(order)
admin.site.register(user)
