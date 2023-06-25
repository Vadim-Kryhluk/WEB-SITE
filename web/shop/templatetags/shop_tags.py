from django import template
from shop.models import *

register = template.Library()

@register.simple_tag(name='get_cats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('shop/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}