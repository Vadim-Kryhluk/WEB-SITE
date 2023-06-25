from .models import *

menu = [{'title': 'Головна сторінка', 'url_name': 'home'},
        {'title': 'Інформація про сайт', 'url_name': 'about_shop'},
        {'title': 'Наші контакти', 'url_name': 'contacts'},
      ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context