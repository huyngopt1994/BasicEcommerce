
from django.template import  Library
from August.August.setting import MEDIA_URL

register =  Library()

@register.simple_tag
def media_url():
    return MEDIA_URL