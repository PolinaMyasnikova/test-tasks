from django import template
from women.models import *

register = template.Library()

@register.simple_tag(name="getvill")
def get_villages(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_villages.html')
def show_villages(vil_selected=0):
    vill = Category.objects.all()
    return {"vill": vill, "vil_selected": vil_selected}

@register.inclusion_tag('women/menu.html')
def show_menu():
    menu = [{'title': "О сайте", 'url_name': 'about'},
            {'title': "Добавить статью", 'url_name': 'add_page'},
            {'title': "Обратная связь", 'url_name': 'contact'},
            {'title': "Войти", 'url_name': 'login'},
            ]
    return {'menu': menu}

