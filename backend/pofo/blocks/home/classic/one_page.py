"""
Module: pofo.blocks.classic.one_page.py
Description:

Created by: Omer Faruk (OFO) Ozyurt
Creation Date: 2025-11-02

Developers:
    - Omer Faruk (OFO) Ozyurt

Notes:
    IMPORTANT:
    If you are not one of the developers listed above, please consult with them
    before making any changes to this module.
    This helps ensure that any modifications align with the module's intended
    design and use cases.

    All blocks in this module are adopted DIRECTLY from POFO's
        Home -> Classic -> One Page.
    Can be Accessed at: https://pofo.themezaa.com/home-classic-one-page/
    Last Accessed: 2025-11-02
Changelog:
    - <Date>: <Description of significant changes>

"""

# region Imports
# region Python Imports
from __future__ import annotations
import logging
import uuid

# endregion Python Imports

# region Django Imports
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
# endregion Django Imports

# region ThirdParty Imports
from wagtail.blocks import (
    StructBlock, CharBlock, RichTextBlock,
    BooleanBlock, ListBlock
)
from wagtail.images.blocks import ImageChooserBlock

# endregion ThirdParty Imports

# region Dev Imports
# endregion Dev Imports

# endregion Imports

logger = logging.getLogger(__name__)

__all__ = [
    "AccordionBlock",
]

BLOCK_GROUP = "POFO - Home - Classic - One Page"


class AccordionItemBlock(StructBlock):
    title = CharBlock(
        required=True,
        help_text=_("Accordion item title")
    )
    body = RichTextBlock(
        features=["bold", "italic", "ol", "ul", "link"],
        help_text=_("Accordion item content")
    )
    open_by_default = BooleanBlock(
        required=False,
        default=False,
        help_text=_("Expanded on load?")
    )

    class Meta:
        icon = "list-ul"
        label = "Accordion Item"


class AccordionBlock(StructBlock):
    """
    Adopted from POFO's Classic One Page

    Available at: https://pofo.themezaa.com/home-classic-one-page/
    Last Accessed: 2025-11-01
    """
    eyebrow = CharBlock(
        required=False,
        help_text=_("Small line above the heading")
    )
    heading = RichTextBlock(
        required=True,
        help_text=_("Main heading")
    )
    image = ImageChooserBlock(
        required=True,
        help_text=_("Right-side background image")
    )
    items = ListBlock(
        AccordionItemBlock(),
        min_num=1
    )

    # Optional presentation tweaks you can expose to editors
    section_classes = CharBlock(
        required=False,
        default="bg-light-gray border-none p-0 wow animate__fadeIn"
    )
    left_col_classes = CharBlock(
        required=False,
        default=(
            "col padding-seven-lr padding-six-half-tb lg-padding-five-tb "
            "lg-padding-six-lr md-padding-six-all sm-padding-50px-tb "
            "sm-padding-15px-lr wow animate__fadeInLeft"
        )
    )
    right_col_classes = CharBlock(
        required=False,
        default=(
            "col cover-background md-h-500px sm-h-350px "
            "wow animate__fadeInRight"
        )
    )
    accordion_style_classes = CharBlock(
        required=False,
        default="panel-group accordion-event accordion-style2"
    )
    anchor_id = CharBlock(
        required=False,
        help_text=_("Optional HTML id for the section")
    )

    class Meta:
        template = "pofo/blocks/home/classic/onepage/accordion.html"
        group = BLOCK_GROUP
        label = "Accordion"

    # give each rendered instance a stable unique id to keep collapse
    # ids unique on a page
    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context=parent_context)
        # prefer a deterministic id from heading, fall back to uuid
        base = slugify(value.get("heading") or "")[:30]
        ctx["block_uid"] = base or uuid.uuid4().hex[:8]
        return ctx
