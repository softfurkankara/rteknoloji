"""
Module:
Description:

Created by: Furkan (FK) KARA
Creation Date: 2025-07-17

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
from ..models import HomePage

# Third Party BEGIN

# Imports END
register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_logo(context):
    try:
        return HomePage.objects.first()
    except Exception:
        return None
