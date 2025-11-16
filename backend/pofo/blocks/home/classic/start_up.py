"""
Module: pofo.blocks.home.classic.start_up.py
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
        Home -> Classic -> Start Up.
    Can be Accessed at: https://pofo.themezaa.com/home-classic-start-up/
    Last Accessed: 2025-11-02

Changelog:
    - <Date>: <Description of significant changes>

"""

# region Imports
# region Python Imports
from __future__ import annotations
import logging
# endregion Python Imports

# region Django Imports
from django.utils.translation import gettext_lazy as _
# endregion Django Imports

# region ThirdParty Imports
from wagtail.blocks import (
    StructBlock, CharBlock, RichTextBlock,
    BooleanBlock, ListBlock, ChoiceBlock
)
from wagtail.images.blocks import ImageChooserBlock

# endregion ThirdParty Imports

# region Dev Imports
# endregion Dev Imports

# endregion Imports

logger = logging.getLogger(__name__)

__all__ = [
    "InformationBlock",
]

BLOCK_GROUP = "POFO - Home - Classic - Start Up"


class InfoBoxItemBlock(StructBlock):
    title = CharBlock(required=True)
    text = RichTextBlock(
        features=["bold", "italic", "ol", "ul", "link"], required=True
    )
    image = ImageChooserBlock(required=True)
    text_first = BooleanBlock(
        required=False, default=False,
        help_text=_(
            "Place the text above and image below (like the middle example)."
        )
    )
    arrow = ChoiceBlock(
        choices=[("top", "Arrow Top"), ("bottom", "Arrow Bottom")],
        default="top",
        help_text=_("Decorative arrow on the text block.")
    )
    show_separator = BooleanBlock(required=False, default=True)
    separator_class = CharBlock(
        required=False,
        default=(
            "separator-line-horrizontal-medium-light2 bg-deep-pink "
            "d-inline-block margin-40px-top sm-margin-20px-top"
        ),
        help_text=_("Classes for the little colored separator line.")
    )

    class Meta:
        icon = "placeholder"
        label = "Info Box Item"


class InformationBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Start-Up Page

    Available at: https://pofo.themezaa.com/home-classic-start-up/
    Last Accessed: 2025-11-01
    """
    items = ListBlock(
        InfoBoxItemBlock(),
        min_num=1,
        max_num=3,
        help_text=_("Add 1–3 items")
    )
    # layout / style knobs (override per instance if needed)
    section_classes = CharBlock(
        required=False,
        default="py-0 bg-light-gray wow animate__fadeIn"
    )
    container_classes = CharBlock(
        required=False,
        default="container-fluid p-0"
    )
    row_classes = CharBlock(
        required=False,
        default="row row-cols-1 row-cols-lg-3 justify-content-center g-0"
    )
    col_classes = CharBlock(
        required=False,
        default=(
            "col image-hover-style-3 last-paragraph-no-margin bg-light-gray"
        )
    )
    img_wrapper_classes = CharBlock(
        required=False,
        default=(
            "w-100 d-table position-relative cover-background small-screen "
            "sm-h-300px"
        )
    )
    text_wrapper_base = CharBlock(
        required=False,
        default="w-100 small-screen sm-h-300px d-table"
    )
    text_inner_classes = CharBlock(
        required=False,
        default=(
            "d-table-cell align-middle padding-eighteen-lr xl-padding-nine-lr "
            "lg-padding-twelve-lr text-center md-padding-ten-lr "
            "sm-padding-seven-all"
        )
    )
    title_classes = CharBlock(
        required=False,
        default=(
            "text-extra-dark-gray alt-font w-95 mx-auto md-w-100 "
            "sm-margin-15px-bottom"
        )
    )

    class Meta:
        template = "pofo/blocks/home/classic/startup/information.html"
        group = BLOCK_GROUP
        label = "Information"
