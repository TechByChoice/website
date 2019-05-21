from __future__ import unicode_literals
from django import template

from wagtail.contrib.modeladmin.options import ModelAdmin

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page

@register.inclusion_tag('home/tags/header.html', takes_context=True)
def header(context, self):
    self = self
    return {
        'self': self,
        'request': context['request'],
    }

@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer(context, self):
    self = self
    return {
        'self': self,
        'request': context['request'],
    }
