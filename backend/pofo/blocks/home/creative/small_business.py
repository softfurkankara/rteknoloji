"""
Module: pofo.blocks.home.creative.small_business.py
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
        Home -> Creative -> Small Business.
    Can be Accessed at: https://pofo.themezaa.com/home-creative-small-business/
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
    BooleanBlock, DecimalBlock, PageChooserBlock,
    URLBlock, ListBlock, IntegerBlock
)
from wagtail.images.blocks import ImageChooserBlock

# endregion ThirdParty Imports

# region Dev Imports
# endregion Dev Imports

# endregion Imports

logger = logging.getLogger(__name__)

__all__ = [
    "ServicesBlock",
    "ClientsBlock",
]

BLOCK_GROUP = "POFO - Home - Creative - Small Business"


class ServicesBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Creative Small Business Page

    Available at: https://pofo.themezaa.com/home-creative-small-business/
    Last Accessed: 2025-11-01
    """
    heading = RichTextBlock(
        features=["bold", "italic", "link"],
        help_text=_("Main headline; supports <strong> for emphasis.")
    )
    background = ImageChooserBlock(
        help_text=_("Background image (large, wide).")
    )
    parallax_ratio = DecimalBlock(
        default=0.5,
        min_value=0, max_value=1,
        help_text=_("data-parallax-background-ratio")
    )
    background_position = CharBlock(
        required=False,
        default="center center",
        help_text=_("CSS background-position.")
    )
    show_overlay = BooleanBlock(required=False, default=True)
    overlay_classes = CharBlock(
        required=False,
        default="opacity-extra-medium bg-black"
    )

    # layout/style knobs
    section_classes = CharBlock(
        required=False,
        default=(
            "wow animate__fadeIn parallax sm-background-image-center "
            "padding-nineteen-bottom sm-padding-50px-bottom"
        )
    )
    container_classes = CharBlock(
        required=False,
        default=(
            "container-fluid padding-thirteen-lr lg-padding-six-lr "
            "position-relative sm-padding-15px-lr"
        )
    )
    row_classes = CharBlock(
        required=False,
        default="row justify-content-center"
    )
    col_classes = CharBlock(
        required=False,
        default="col-sm-8 col-xxl-6 text-center"
    )
    heading_classes = CharBlock(
        required=False,
        default="text-white-2 alt-font font-weight-300 sm-margin-5px-bottom"
    )

    anchor_id = CharBlock(
        required=False, help_text=_("Optional #id for the section")
    )

    class Meta:
        template = "pofo/blocks/home/creative/smallbusiness/services.html"
        group = BLOCK_GROUP
        label = "Services"


class LogoItemBlock(StructBlock):
    image = ImageChooserBlock(
        required=True,
        help_text=_("Partner/client logo")
    )
    alt_text = CharBlock(
        required=False,
        help_text=_("Accessible alt text (defaults to image title)")
    )
    page = PageChooserBlock(
        required=False,
        help_text=_("Internal link (optional)")
    )
    url = URLBlock(required=False, help_text=_("External link (optional)"))
    open_in_new_tab = BooleanBlock(required=False, default=False)
    item_extra_classes = CharBlock(
        required=False,
        help_text=_("Extra classes for this logo’s column (optional)")
    )

    class Meta:
        icon = "image"
        label = "Logo"


class ClientsBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Creative Small Business Page

    Available at: https://pofo.themezaa.com/home-creative-small-business/
    Last Accessed: 2025-11-01
    """
    items = ListBlock(LogoItemBlock(), min_num=1)

    # layout/style knobs (defaults mirror your snippet)
    section_classes = CharBlock(
        required=False,
        default="wow animate__fadeIn overlap-section no-padding-top z-index-5"
    )
    container_classes = CharBlock(
        required=False,
        default=(
            "container-fluid padding-thirteen-lr lg-padding-six-lr "
            "sm-no-padding-lr"
        )
    )
    outer_row_classes = CharBlock(required=False, default="row")
    full_col_classes = CharBlock(required=False, default="col-12")
    logos_row_classes = CharBlock(
        required=False,
        default=(
            "row row-cols-1 row-cols-md-3 row-cols-sm-2 align-items-center "
            "m-0 bg-medium-light-gray padding-100px-tb padding-90px-lr "
            "md-padding-60px-tb md-padding-30px-lr"
        )
    )
    logo_col_classes = CharBlock(
        required=False,
        default=(
            "col text-center margin-ten-bottom md-margin-six-bottom "
            "sm-margin-10px-bottom"
        )
    )

    # image rendition control
    # TODO: Currently not implemented at the template needed.
    logo_width = IntegerBlock(
        required=False,
        default=220,
        help_text=_("Rendered width for logos (px)")
    )

    anchor_id = CharBlock(
        required=False,
        help_text=_("Optional #id for the section")
    )

    class Meta:
        template = "pofo/blocks/home/creative/smallbusiness/clients.html"
        group = "POFO - Home - Creative - Small Business"
        label = "Clients"
