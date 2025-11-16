"""
Module:
Description:

Created by: Furkan (FK) KARA
Creation Date:

Developers:
    - Furkan (FK) KARA

Notes:
    IMPORTANT:
    If you are not one of the developers listed above, please consult with them
    before making any changes to this module.
    This helps ensure that any modifications align with the module's intended
    design and use cases.

Changelog:
    - <Date>: <Description of significant changes>

"""
# Imports BEGIN


# Python Built-in Imports START

# Django Built-in Imports START
from django import template

# Devs Import START

# Third Party BEGIN
from wagtail.models import Site

# Imports END
register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context['request']).root_page
