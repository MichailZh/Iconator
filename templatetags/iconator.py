from django import template

register = template.Library()


@register.simple_tag()
def iconator(name):
    with open("Iconator/" + "icons" + "/" + name + ".svg", 'r') as file:
        data = file.read()
        return data