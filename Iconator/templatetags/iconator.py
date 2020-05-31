from django import template
import os.path

register = template.Library()


@register.simple_tag()
def iconator(name):
    rel_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(rel_path, "icons"+ "\\" + name + ".svg")
    with open(path, 'r') as file:
        data = file.read()
        return data