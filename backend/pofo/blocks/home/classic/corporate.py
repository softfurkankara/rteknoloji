"""
Module: pofo.blocks.home.classic.corporate.py
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
        Home -> Classic -> Corporate.
    Can be Accessed at: https://pofo.themezaa.com/home-classic-corporate/
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
    StructBlock, CharBlock, PageChooserBlock,
    URLBlock, RichTextBlock, BooleanBlock,
    ListBlock, IntegerBlock, TextBlock, ChoiceBlock
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

# endregion ThirdParty Imports

# region Dev Imports
# endregion Dev Imports

# endregion Imports

logger = logging.getLogger(__name__)

__all__ = [
    "SlidersBlock",
    "AboutBlock",
    "ServicesWIconBlock",
    "FeaturePairsBlock",
    "PortfolioBlock",
    "InformationBlock",
    "ParallaxFeatureBlock",
    "ServicesGalleryBlock",
    "ParallaxBlock",
    "ServicesWFeaturesBlock",
]

BLOCK_GROUP = "POFO - Home - Classic - Corporate"


class CTAButtonBlock(StructBlock):
    """Config for an optional CTA button on a slide."""
    label = CharBlock(label=_("Label"), help_text=_("Button text"))
    page = PageChooserBlock(
        required=False, label=_("Internal page"),
        help_text=_("If both page and URL are set, 'page' wins.")
    )
    url = URLBlock(required=False, label=_("External URL"))
    classes = CharBlock(
        required=False, label=_("Classes"),
        help_text=_(
            "Append POFO/Bootstrap classes, e.g. 'btn-medium border-radius-4'."
        ),
        default=(
            "tp-caption btn btn-transparent-white btn-medium border-radius-4 "
            "z-index-5"
        ),
        search_index=False
    )

    class Meta:
        collapsed = True
        label = _("CTA Button")


class POFOSlideBlock(StructBlock):
    """A single POFO hero slide."""
    background = ImageChooserBlock(label=_("Background image"))

    # region Background video
    use_video = BooleanBlock(
        required=False, default=False,
        label=_("Use background video")
    )
    video_file = DocumentChooserBlock(
        required=False,
        label=_("Video (MP4) – internal")
    )
    video_url = URLBlock(
        required=False, label=_("Video URL (MP4) – external")
    )
    video_preload = ChoiceBlock(
        required=False,
        default="auto",
        choices=[("auto", "auto"), ("metadata", "metadata"), ("none", "none")],
        label=_("Video preload"),
    )
    video_loop = BooleanBlock(
        required=False, default=True, label=_("Loop video")
    )
    video_muted = BooleanBlock(
        required=False, default=True, label=_("Muted (autoplay-safe)")
    )
    video_autoplay = BooleanBlock(
        required=False, default=True, label=_("Autoplay")
    )
    video_playsinline = BooleanBlock(
        required=False, default=True, label=_("Plays inline (mobile)")
    )
    video_forcerewind = BooleanBlock(
        required=False, default=True, label=_("Force rewind at slide start")
    )
    video_startat = IntegerBlock(
        required=False, default=0, label=_("Start at (seconds)")
    )
    # endregion Background video

    eyebrow = CharBlock(
        required=False, label=_("Eyebrow / small heading"),
        help_text=_("E.g. 'we work hard, we play hard'.")
    )
    eyebrow_classes = CharBlock(
        required=False, default="NotGeneric-Title",
        help_text=_("POFO/Revolution caption class for the eyebrow."),
        search_index=False
    )
    title = RichTextBlock(
        required=False,
        help_text=_("Rich text is allowed. Use Shift+Enter for line breaks."),
        label=_("Main title"),
        features=["bold", "italic", "link", "br"],
    )
    title_classes = CharBlock(
        required=False, default="NotGeneric-SubTitle",
        help_text=_("POFO/Revolution caption class for the title."),
        search_index=False
    )
    cta = CTAButtonBlock(required=False, label=_("CTA Button"))
    masterspeed = IntegerBlock(
        required=True, default=1000,
        help_text=_("Animation speed in milliseconds.")
    )
    dark_overlay = BooleanBlock(
        required=False, default=True, label=_("Dark overlay"),
        help_text=_("Adds POFO 'opacity-extra-medium bg-black' overlay.")
    )
    thumb = ImageChooserBlock(
        required=False, label=_("Bullet thumbnail"),
        help_text=_("Used in slider bullets if enabled.")
    )
    transition = CharBlock(
        required=False, default="fade",
        help_text=_("Transition effect for the slide."),
        search_index=False
    )
    slotamount = CharBlock(
        required=False, default="default",
        search_index=False
    )
    hideafterloop = IntegerBlock(
        required=False, default=0,
        search_index=False
    )
    hideslideonmobile = CharBlock(
        required=False, default="off",
        search_index=False
    )
    easein = CharBlock(
        required=False, default="Power4.easeInOut",
        search_index=False
    )
    easeout = CharBlock(
        required=False, default="Power4.easeInOut",
        search_index=False
    )
    rotate = IntegerBlock(
        required=False, default=0,
        search_index=False
    )

    class Meta:
        collapsed = True
        label = _("POFO Hero Slide")


class SlidersBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-02
    """
    section_classes = CharBlock(
        required=False,
        default="wow animate__fadeIn no-padding no-transition",
        help_text=_("Classes applied to the outer <section>."),
        search_index=False
    )
    show_bullets = BooleanBlock(
        required=False, default=True, label=_("Show bullets")
    )
    slides = ListBlock(POFOSlideBlock(), label=_("Slides"), min_num=1)

    slider_dom_id = CharBlock(
        required=False, default="rev_slider_home_corporate",
        help_text=_("DOM id for the slider, keep unique per page."),
        search_index=False
    )

    class Meta:
        template = "pofo/blocks/home/classic/corporate/sliders.html"
        group = BLOCK_GROUP
        label = "Sliders"


class FeatureBoxItemBlock(StructBlock):
    icon_class = CharBlock(
        required=False,
        default=(
            "icon-tools icon-extra-medium text-deep-pink margin-20px-bottom"
        ),
        search_index=False
    )
    title = CharBlock()
    text = TextBlock()
    wow_delay = CharBlock(required=False, search_index=False)

    class Meta:
        icon = "placeholder"
        label = "Feature Item"


class AboutBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-03
    """
    section_classes = CharBlock(
        required=False,
        default=(
            "wow animate__fadeIn overflow-hidden cover-background "
            "md-no-background-img bg-medium-light-gray"
        ),
        search_index=False
    )
    background_image = ImageChooserBlock(required=False)
    background_fallback_url = URLBlock(
        required=False,
        default="https://via.placeholder.com/1920x800"
    )
    content_col_classes = CharBlock(
        required=False,
        default="col-12 col-lg-6 offset-lg-6 wow animate__fadeIn",
        search_index=False
    )
    eyebrow = CharBlock(required=False)
    heading = CharBlock(required=True)
    description = TextBlock(required=False)
    features = ListBlock(FeatureBoxItemBlock(), min_num=1, max_num=2)

    class Meta:
        template = "pofo/blocks/home/classic/corporate/about.html"
        group = BLOCK_GROUP
        label = "About"


class ServiceWIconItemBlock(StructBlock):
    title = CharBlock()
    text = TextBlock(required=False)
    icon_class = CharBlock(
        required=False,
        default="icon-tools text-white-2 icon-round-small bg-deep-pink",
        search_index=False
    )

    class Meta:
        collapsed = True
        label = "Service Item"


class ServicesWIconBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-03

    ServicesWIconBlock => Services With Icon Block
    If you search where this block originally located at the POFO's Classic
    Corporate Page, this is the first "section" with naming "services". If you
    want to visually see it, this section has 4 cards with an icon on
    top of them.
    """
    heading = CharBlock(required=True)
    description = TextBlock(required=False)
    section_classes = CharBlock(
        required=False,
        default="overflow-hidden wow animate__fadeIn",
        search_index=False
    )
    container_classes = CharBlock(
        required=False,
        default="container",
        search_index=False
    )
    intro_col_classes = CharBlock(
        required=False,
        default=(
            "col-lg-8 margin-eight-bottom text-center last-paragraph-no-margin"
        ),
        search_index=False
    )
    row_classes = CharBlock(
        required=False,
        default="row row-cols-1 row-cols-lg-4 row-cols-sm-2",
        search_index=False
    )
    items = ListBlock(ServiceWIconItemBlock(), min_num=1, max_num=4)

    class Meta:
        template = "pofo/blocks/home/classic/corporate/services_wicon.html"
        group = BLOCK_GROUP
        label = "Services With Icon"

    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context=parent_context)
        col_seq = [
            "col md-margin-30px-bottom xs-margin-15px-bottom wow animate__fadeInUp last-paragraph-no-margin",
            "col md-margin-30px-bottom xs-margin-15px-bottom wow animate__fadeInUp last-paragraph-no-margin",
            "col xs-margin-15px-bottom wow animate__fadeInUp last-paragraph-no-margin",
            "col wow animate__fadeInUp last-paragraph-no-margin",
        ]
        delay_seq = ["", "0.2s", "0.4s", "0.6s"]
        decorated = []
        for i, item in enumerate(value["items"]):
            decorated.append({
                "item"       : item,
                "col_classes": col_seq[i % len(col_seq)],
                "wow_delay"  : delay_seq[i % len(delay_seq)],
            })
        ctx["items_decorated"] = decorated
        return ctx


class FeaturePairItemBlock(StructBlock):
    # LEFT: image
    background_image = ImageChooserBlock(required=False)
    background_fallback_url = URLBlock(
        required=False,
        default="https://via.placeholder.com/850x813"
    )
    # RIGHT: content
    eyebrow = CharBlock(required=False)
    heading = CharBlock(required=True)
    text = TextBlock(required=False)
    button_label = CharBlock(required=False, search_index=False)
    button_url = URLBlock(required=False)

    class Meta:
        icon = "placeholder"
        label = "Feature Pair (Image + Content)"


class FeaturePairsBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-03

    If you search where this block originally located at the POFO's Classic
    Corporate Page, this is the "section" actually has no name.
    """
    items = ListBlock(FeaturePairItemBlock(), min_num=1)
    # POFO default col classes kept intact (not editor-exposed)
    image_col_classes = CharBlock(
        required=False,
        default=(
            "col p-0 cover-background position-relative sm-h-450px xs-h-350px "
            "wow animate__fadeIn"
        ),
        search_index=False
    )
    content_col_classes = CharBlock(
        required=False,
        default=(
            "col p-0 d-flex align-items-center position-relative "
            "bg-extra-dark-gray text-center text-md-start wow animate__fadeIn"
        ),
        search_index=False
    )

    section_classes = CharBlock(
        required=False,
        default="p-0 wow animate__fadeIn",
        search_index=False
    )
    container_classes = CharBlock(
        required=False,
        default="container-fluid",
        search_index=False
    )
    row_classes = CharBlock(
        required=False,
        default="row row-cols-1 row-cols-xl-4 row-cols-md-2 row-cols-sm-1",
        search_index=False
    )

    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context=parent_context)

        # Compute WOW delays per pair: (image: +0.0s, content: +0.2s), then (image: +0.4s, content: +0.6s), etc.
        decorated = []
        base_image_classes = value.get("image_col_classes")
        base_content_classes = value.get("content_col_classes")
        for i, pair in enumerate(value["items"]):
            base = i * 0.4  # 0.0, 0.4, 0.8, ...
            image_delay = "" if base == 0 else f"{base:.1f}s"
            content_delay = f"{base + 0.2:.1f}s"
            decorated.append(
                {
                    "pair"           : pair,
                    "image_classes"  : base_image_classes,
                    "content_classes": base_content_classes,
                    "image_delay"    : image_delay,
                    "content_delay"  : content_delay,
                }
            )
        ctx["pairs"] = decorated
        return ctx

    class Meta:
        template = "pofo/blocks/home/classic/corporate/feature_pairs.html"
        group = BLOCK_GROUP
        label = "Feature Pairs"


class PortfolioFilterOptionBlock(StructBlock):
    label = CharBlock()
    slug = CharBlock(help_text="Filter slug without dot, e.g. 'web'")

    class Meta:
        icon = "tag"
        label = "Filter Option"


class PortfolioItemBlock(StructBlock):
    title = CharBlock(required=True)
    subtitle = CharBlock(required=False, default="Category and Type")
    image = ImageChooserBlock(required=False)
    image_fallback_url = URLBlock(required=False, default="https://via.placeholder.com/800x650")
    # page supress link_url
    page = PageChooserBlock(required=False)
    link_url = URLBlock(required=False, default="single-project-page-01.html")
    tags = ListBlock(
        CharBlock(
            help_text="Filter slugs, e.g. web, branding, design",
            search_index=False,
        ),
        required=False,
    )

    class Meta:
        icon = "image"
        label = "Portfolio Item"


class PortfolioBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-07

    If you search where this block originally located at the POFO's Classic
    Corporate Page, this is the "section" actually has no name.
    """
    filters = ListBlock(PortfolioFilterOptionBlock(), required=False)
    items = ListBlock(PortfolioItemBlock(), min_num=1)

    section_classes = CharBlock(
        required=False,
        default=(
            "wow animate__fadeIn padding-90px-top md-padding-50px-top "
            "sm-padding-30px-top pb-0"
        ),
        search_index=False
    )
    container_classes = CharBlock(
        required=False,
        default="container",
        search_index=False
    )
    filter_ul_classes = CharBlock(
        required=False,
        default=(
            "portfolio-filter nav nav-tabs justify-content-center border-0 "
            "portfolio-filter-tab-1 font-weight-600 alt-font text-uppercase "
            "text-center margin-80px-bottom text-small md-margin-40px-bottom "
            "sm-margin-20px-bottom"
        ),
        search_index=False
    )
    grid_container_classes = CharBlock(
        required=False,
        default="container-fluid",
        search_index=False
    )
    grid_ul_classes = CharBlock(
        required=False,
        default=(
            "hover-option7 portfolio-wrapper grid grid-loading grid-4col "
            "xl-grid-4col lg-grid-3col md-grid-2col sm-grid-2col xs-grid-1col "
            "gutter-medium"
        ),
        search_index=False
    )

    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context=parent_context)

        # wow delays: "", 0.2s, 0.4s, 0.6s, repeat
        delays = ["", "0.2s", "0.4s", "0.6s"]
        decorated = []
        for i, item in enumerate(value["items"]):
            tag_classes = " ".join(item.get("tags", []))
            decorated.append({
                "item"      : item,
                "li_classes": f"grid-item {tag_classes} wow animate__fadeInUp".strip(),
                "wow_delay" : delays[i % len(delays)],
            })
        ctx["items_decorated"] = decorated

        # filters to render: All + provided filters (or inferred unique tags if filters empty)
        filt = list(value.get("filters") or [])
        if not filt:
            # infer unique tags from items
            seen = []
            for it in value["items"]:
                for t in it.get("tags", []):
                    if t not in seen:
                        seen.append(t)
            filt = [{"label": t.title(), "slug": t} for t in seen]
        ctx["filters_decorated"] = filt
        return ctx

    class Meta:
        template = "pofo/blocks/home/classic/corporate/portfolio.html"
        group = BLOCK_GROUP
        label = "Portfolio Grid"


class InformationBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-08

    You can search this with the "information" section
    """
    heading = CharBlock(
        required=True,
        default="Beautifully handcrafted templates for your website",
    )
    bullets = ListBlock(
        CharBlock(), min_num=1, default=[
            "Beautiful and easy to understand UI, professional animations",
            "Theme advantages are pixel perfect design & clear code delivered",
            "Present your services with flexible, convenient and multipurpose",
            "Find more creative ideas for your projects",
            "Unlimited power and customization possibilities",
        ]
    )

    button_label = CharBlock(
        required=False, default="ALL advantages"
    )
    button_page = PageChooserBlock(required=False)
    button_url = URLBlock(
        required=False, default="home-classic-digital-agency.html"
    )

    image = ImageChooserBlock(required=False)
    image_alt = CharBlock(required=False, default="")
    image_fallback_url = URLBlock(
        required=False, default="https://via.placeholder.com/1200x700"
    )
    # region HTML/CSS Classes
    section_classes = CharBlock(
        required=False, default="wow animate__fadeIn", search_index=False
    )
    container_classes = CharBlock(
        required=False, default="container", search_index=False
    )
    row_classes = CharBlock(
        required=False, default="row align-items-center", search_index=False
    )
    left_col_classes = CharBlock(
        required=False, default="col-lg-5 md-margin-50px-bottom"
    )
    bullet_list_classes = CharBlock(
        required=False, default="p-0 list-style-4", search_index=False
    )
    button_classes = CharBlock(
        required=False,
        default=(
            "btn btn-dark-gray btn-small text-extra-small border-radius-4 "
            "margin-20px-top"
        ),
        search_index=False,
    )
    button_icon_classes = CharBlock(
        required=False,
        default=(
            "fa-solid fa-circle-play icon-very-small margin-5px-right "
            "no-margin-left"
        ),
        search_index=False,
    )
    right_col_classes = CharBlock(
        required=False, default="col-lg-7 text-center", search_index=False
    )
    image_classes = CharBlock(
        required=False, default="w-100", search_index=False
    )

    # endregion HTML/CSS Classes
    class Meta:
        template = "pofo/blocks/home/classic/corporate/information.html"
        group = BLOCK_GROUP
        label = "Information"


class ParallaxFeatureListItemBlock(StructBlock):
    title = CharBlock(required=True, default="Powerful Website Builder")
    text = TextBlock(
        required=False,
        default=(
            "Lorem Ipsum is simply dummy text of the printing and "
            "typesetting industry."
        )
    )
    icon_class = CharBlock(
        required=False,
        default="icon-desktop text-medium-gray icon-medium",
        search_index=False
    )

    class Meta:
        icon = "placeholder"
        label = "Feature List Item"


class ParallaxFeatureBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-08

    You can search this with the "parallax feature" section
    """
    heading = CharBlock(
        required=True,
        default="We are delivering beautiful digital products for you"
    )
    feature_col_seq = ListBlock(
        CharBlock(),
        required=False,
        default=[
            "col margin-six-bottom md-margin-50px-bottom sm-margin-40px-bottom last-paragraph-no-margin",
            "col margin-six-bottom md-margin-50px-bottom sm-margin-40px-bottom last-paragraph-no-margin",
            "col lg-margin-six-bottom sm-margin-40px-bottom last-paragraph-no-margin",
            "col last-paragraph-no-margin",
        ],
        help_text=_(
            "Repeating sequence of column classes applied per feature item."
        ),
    )
    items = ListBlock(
        ParallaxFeatureListItemBlock(),
        min_num=1,
        default=[
            {"icon_class": "icon-desktop text-medium-gray icon-medium", "title": "Powerful Website Builder",
             "text"      : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since."},
            {"icon_class": "icon-book-open text-medium-gray icon-medium", "title": "Different Layout Type",
             "text"      : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since."},
            {"icon_class": "icon-wallet text-medium-gray icon-medium", "title": "True Responsiveness",
             "text"      : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since."},
            {"icon_class": "icon-camera text-medium-gray icon-medium", "title": "Elegant / Unique design",
             "text"      : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since."},
        ],
    )

    # Right column (background image)
    right_col_classes = CharBlock(required=False,
                                  default="col cover-background md-h-400px wow animate__fadeInRight")
    right_background_image = ImageChooserBlock(required=False)
    right_background_fallback_url = URLBlock(required=False, default="https://via.placeholder.com/945x663")

    # region HTML/CSS Classes
    # Section / layout
    section_classes = CharBlock(
        required=False,
        default="p-0 wow animate__FadeIn bg-light-gray",
        search_index=False
    )
    container_classes = CharBlock(
        required=False,
        default="container-fluid",
        search_index=False
    )
    row_classes = CharBlock(
        required=False,
        default="row row-cols-1 row-cols-lg-2",
        search_index=False
    )
    # Left column (features)
    left_col_classes = CharBlock(
        required=False,
        default=(
            "col wow animate__fadeInLeft padding-four-all md-padding-eight-all "
            "md-padding-15px-lr sm-padding-50px-tb"
        ),
        search_index=False
    )
    heading_wrapper_classes = CharBlock(
        required=False,
        default="row m-0",
        search_index=False
    )
    heading_col_classes = CharBlock(
        required=False,
        default=(
            "col-xl-10 margin-six-bottom lg-margin-six-bottom "
            "md-margin-30px-bottom sm-no-margin-bottom"
        ),
        search_index=False
    )
    heading_classes = CharBlock(
        required=False,
        default=(
            "alt-font text-extra-dark-gray font-weight-600 text-center "
            "text-lg-start md-w-70 mx-auto mx-lg-0 sm-w-90 xs-w-100 "
            "sm-margin-30px-bottom"
        ),
        search_index=False
    )
    features_row_classes = CharBlock(
        required=False,
        default="row row-cols-1 row-cols-xl-2 row-cols-lg-1 row-cols-sm-2 m-0",
        search_index=False
    )

    # endregion HTML/CSS Classes

    class Meta:
        template = "pofo/blocks/home/classic/corporate/parallax_feature.html"
        group = BLOCK_GROUP
        label = "Parallax Feature"

    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context=parent_context)
        delays = ["", "0.2s", "0.4s", "0.6s"]
        col_seq = value.get("feature_col_seq") or []
        decorated = []
        for i, item in enumerate(value["items"]):
            col_classes = col_seq[i % len(col_seq)] if col_seq else "col"
            decorated.append(
                {
                    "item"       : item,
                    "col_classes": col_classes,
                    "wow_delay"  : delays[i % len(delays)],
                }
            )
        ctx["items_decorated"] = decorated
        return ctx


class ServiceGalleryItemBlock(StructBlock):
    title = CharBlock(required=True, default="Design and Development")
    image = ImageChooserBlock(required=False)
    image_fallback_url = URLBlock(
        required=False, default="https://via.placeholder.com/900x650"
    )
    hover_text = CharBlock(required=False, search_index=False)
    statline = CharBlock(required=False, default="600+ We created web design")

    class Meta:
        icon = "image"
        label = "Service Gallery Item"


class ServicesGalleryBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-08

    You can search this with the "services" section
    """
    heading = CharBlock(required=True, default="our services")
    eyebrow = CharBlock(
        required=False,
        default="What We Do",
        search_index=False
    )
    items = ListBlock(
        ServiceGalleryItemBlock(),
        min_num=1,
        default=[
            {
                "title"             : "Design and Development",
                "statline"          : "600+ We created web design",
                "hover_text"        : "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                "image_fallback_url": "https://via.placeholder.com/900x650",
            },
            {
                "title"             : "Social Media Marketing",
                "statline"          : "475+ We completed marketing",
                "hover_text"        : "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                "image_fallback_url": "https://via.placeholder.com/900x650",
            },
            {
                "title"             : "Mobile App Development",
                "statline"          : "475+ We created mobile app",
                "hover_text"        : "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                "image_fallback_url": "https://via.placeholder.com/900x650",
            },
        ],
    )

    # region HTML/CSS Classes
    # Section header
    section_classes = CharBlock(
        required=False,
        default="wow animate__fadeIn",
        search_index=False
    )
    container_classes = CharBlock(
        required=False,
        default="container",
        search_index=False
    )
    header_wrapper_classes = CharBlock(
        required=False,
        default="row",
        search_index=False
    )
    header_col_classes = CharBlock(
        required=False,
        default=(
            "col-12 text-center margin-100px-bottom md-margin-70px-bottom "
            "sm-margin-50px-bottom"
        )
    )
    heading_classes = CharBlock(
        required=False,
        default=(
            "text-uppercase alt-font text-extra-dark-gray margin-20px-bottom "
            "font-weight-700 md-w-100"
        ),
        search_index=False
    )
    separator_classes = CharBlock(
        required=False,
        default=(
            "separator-line-horrizontal-medium-light2 bg-deep-pink d-table "
            "mx-auto w-100px"
        ),
        search_index=False
    )
    # Grid
    grid_row_classes = CharBlock(
        required=False,
        default=(
            "row justify-content-center row-cols-1 row-cols-lg-3 row-cols-md-2"
        ),
        search_index=False
    )
    # In the template they are repressed as "it.col_classes"
    col_seq = ListBlock(
        CharBlock(),
        required=False,
        default=[
            "col-sm-8 team-block text-start feature-box-15 md-margin-40px-bottom last-paragraph-no-margin wow animate__fadeInUp",
            "col-sm-8 team-block text-start feature-box-15 md-margin-40px-bottom last-paragraph-no-margin wow animate__fadeInUp",
            "col-sm-8 team-block text-start feature-box-15 last-paragraph-no-margin wow animate__fadeInUp",
        ],
        help_text=_("Repeating sequence of column classes per item."),
    )

    # endregion HTML/CSS Classes

    class Meta:
        template = "pofo/blocks/home/classic/corporate/services_gallery.html"
        group = BLOCK_GROUP
        label = "Services Gallery"

    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context=parent_context)
        delays = ["", "0.2s", "0.6s"]  # matches example
        col_seq = value.get("col_seq") or []
        decorated = []
        for i, item in enumerate(value["items"]):
            col_classes = col_seq[i % len(col_seq)] if col_seq else "col"
            decorated.append(
                {
                    "item"       : item,
                    "col_classes": col_classes,
                    "wow_delay"  : delays[i % len(delays)],
                }
            )
        ctx["items_decorated"] = decorated
        return ctx


class ParallaxBlock(StructBlock):
    """
    Fundamentally Adopted from POFO's Classic Corporate Page

    Available at: https://pofo.themezaa.com/home-classic-corporate/
    Last Accessed: 2025-11-08

    You can search this with the "parallax" section
    """
    # Background
    background_image = ImageChooserBlock(required=False)
    background_fallback_url = URLBlock(required=False, default="https://via.placeholder.com/1920x1200")
    background_ratio = CharBlock(required=False, default="0.6", search_index=False)

    # Overlay
    show_overlay = BooleanBlock(required=False, default=True)
    overlay_classes = CharBlock(required=False, default="opacity-medium bg-extra-dark-gray", search_index=False)

    # Left image
    left_image = ImageChooserBlock(required=False)
    left_image_fallback_url = URLBlock(required=False, default="https://via.placeholder.com/900x650")
    left_image_alt = CharBlock(required=False, default="", search_index=False)

    # Right content
    heading = CharBlock(required=False, default="Unique, truly responsive and functional websites ")
    text = TextBlock(required=False, default=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since. "
        "Lorem Ipsum has been the industry's standard dummy text."
    ))
    bullets = ListBlock(
        CharBlock(), required=False, default=[
            "Beautiful and easy to understand UI, professional animations",
            "Theme advantages are pixel perfect design & clear code delivered",
            "Present your services with flexible, convenient and multipurpose",
            "Unlimited power and customization possibilities",
        ]
    )

    # Button
    button_label = CharBlock(required=False, default="GET TO KNOW US")
    button_page = PageChooserBlock(required=False)
    button_url = URLBlock(required=False, default="about-us-modern.html")

    # region HTML/CSS classes
    section_classes = CharBlock(required=False, default="parallax", search_index=False)
    container_classes = CharBlock(required=False, default="container-fluid position-relative", search_index=False)
    row_classes = CharBlock(required=False, default="row row-cols-1 row-cols-lg-2 row-cols-md-1 align-items-center",
                            search_index=False)
    left_col_classes = CharBlock(required=False,
                                 default="col text-center md-margin-50px-bottom sm-margin-30px-bottom wow animate__fadeIn",
                                 search_index=False)
    left_image_classes = CharBlock(required=False, default="w-100", search_index=False)

    right_col_classes = CharBlock(required=False, default="col wow animate__fadeIn", search_index=False)
    right_wow_delay = CharBlock(required=False, default="0.2s", search_index=False)
    right_inner_classes = CharBlock(required=False, default="w-75 xl-w-85 lg-w-100 padding-three-lr sm-no-padding-lr",
                                    search_index=False)
    heading_classes = CharBlock(required=False, default="alt-font text-white-2 font-weight-600", search_index=False)
    bullet_list_classes = CharBlock(required=False, default="p-0 list-style-4 margin-30px-bottom list-style-color",
                                    search_index=False)

    button_classes = CharBlock(required=False,
                               default="btn btn-white btn-small text-extra-small border-radius-4 margin-20px-tb md-no-margin-bottom",
                               search_index=False)
    button_icon_classes = CharBlock(required=False,
                                    default="fa-solid fa-circle-play icon-very-small margin-5px-right ms-0",
                                    search_index=False)

    # endregion

    class Meta:
        template = "pofo/blocks/home/classic/corporate/parallax.html"
        group = BLOCK_GROUP
        label = "Parallax Section"


class ServicesWFeatureItemBlock(StructBlock):
    title = CharBlock(required=True, default="Modern Framework")
    text = TextBlock(
        required=False,
        default=(
            "Lorem Ipsum is simply text the printing and typesetting "
            "standard industry."
        )
    )
    icon_class = CharBlock(
        required=False,
        default="icon-desktop text-medium-gray icon-medium",
        search_index=False
    )

    class Meta:
        icon = "placeholder"
        label = "Services Feature Item"


class ServicesWFeaturesBlock(StructBlock):
    """
    Image + content intro with CTA, divider, and a 3-column features grid.

    Mirrors the provided POFO snippet.
    """
    # Intro (top) right content
    heading = CharBlock(
        required=True,
        default="Responsive, convenient and multipurpose theme"
    )
    eyebrow = CharBlock(
        required=False,
        default="Wide range of web development services"
    )
    text = TextBlock(required=False, default=(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since. "
        "Lorem Ipsum has been the industry's standard dummy text ever since. "
        "Lorem Ipsum is printing and typesetting simply dummy text."
    ))

    # Intro (top) left image
    left_image = ImageChooserBlock(required=False)
    left_image_fallback_url = URLBlock(
        required=False, default="https://via.placeholder.com/900x650"
    )
    left_image_alt = CharBlock(required=False, default="", search_index=False)

    # Button
    button_label = CharBlock(
        required=False,
        default="About Company",
        search_index=False
    )
    button_page = PageChooserBlock(required=False)
    button_url = URLBlock(required=False, default="about-us-simple.html")

    # Features list (bottom)
    features = ListBlock(
        ServicesWFeatureItemBlock(), min_num=1, default=[
            {"icon_class": "icon-desktop text-medium-gray icon-medium", "title": "Modern Framework",
             "text"      : "Lorem Ipsum is simply text the printing and typesetting standard industry."},
            {"icon_class": "icon-book-open text-medium-gray icon-medium", "title": "Web Interactive",
             "text"      : "Lorem Ipsum is simply text the printing and typesetting standard industry."},
            {"icon_class": "icon-gift text-medium-gray icon-medium", "title": "Graphic Design",
             "text"      : "Lorem Ipsum is simply text the printing and typesetting standard industry."},
        ]
    )

    # region HTML/CSS classes
    section_classes = CharBlock(
        required=False,
        default="wow animate__fadeIn",
        search_index=False
    )
    container_classes = CharBlock(
        required=False,
        default="container",
        search_index=False
    )

    intro_row_classes = CharBlock(
        required=False,
        default="row align-items-center",
        search_index=False
    )
    left_col_classes = CharBlock(
        required=False,
        default=(
            "col-lg-5 text-center md-margin-50px-bottom wow "
            "animate__fadeInLeft"
        ),
        search_index=False
    )
    right_col_classes = CharBlock(
        required=False,
        default="col-lg-7 wow animate__fadeInRight last-paragraph-no-margin",
        search_index=False
    )
    right_wow_delay = CharBlock(
        required=False,
        default="0.2s",
        search_index=False
    )
    right_inner_classes = CharBlock(
        required=False,
        default="padding-eight-lr text-center text-lg-start sm-no-padding w-100",
        search_index=False
    )

    eyebrow_classes = CharBlock(
        required=False,
        default=(
            "text-deep-pink alt-font margin-10px-bottom md-no-margin-bottom "
            "d-inline-block text-medium"
        ),
        search_index=False
    )
    heading_classes = CharBlock(
        required=False,
        default="font-weight-600 alt-font text-extra-dark-gray",
        search_index=False
    )
    button_classes = CharBlock(
        required=False,
        default=(
            "btn btn-dark-gray btn-small text-extra-small border-radius-4 "
            "margin-30px-top"
        ),
        search_index=False
    )
    button_icon_classes = CharBlock(
        required=False,
        default="fa-solid fa-circle-play icon-very-small margin-5px-right ms-0",
        search_index=False
    )

    divider_classes = CharBlock(
        required=False,
        default=(
            "divider-full bg-extra-light-gray margin-seven-bottom "
            "margin-eight-top"
        ),
        search_index=False
    )

    features_row_classes = CharBlock(
        required=False,
        default="row row-cols-1 row-cols-lg-3 row-cols-sm-2 justify-content-center",
        search_index=False
    )
    feature_col_seq = ListBlock(
        CharBlock(), required=False,
        default=[
            "col md-margin-50px-bottom sm-margin-40px-bottom wow animate__fadeInUp last-paragraph-no-margin",
            "col md-margin-50px-bottom sm-margin-40px-bottom wow animate__fadeInUp last-paragraph-no-margin",
            "col wow animate__fadeInUp last-paragraph-no-margin",
        ],
        help_text=_("Repeating sequence of column classes applied per feature item."),
    )
    feature_text_width_classes = CharBlock(
        required=False,
        default="d-inline-block w-75 lg-w-100 xs-w-90",
        search_index=False
    )

    # endregion

    class Meta:
        template = "pofo/blocks/home/classic/corporate/services_wfeatures.html"
        group = BLOCK_GROUP
        label = "Services With Features"

    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context=parent_context)
        delays = ["", "0.2s", "0.4s"]
        col_seq = value.get("feature_col_seq") or []
        decorated = []
        for i, item in enumerate(value.get("features", [])):
            col_classes = col_seq[i % len(col_seq)] if col_seq else "col"
            decorated.append({
                "item"       : item,
                "col_classes": col_classes,
                "wow_delay"  : delays[i % len(delays)],
            })
        ctx["features_decorated"] = decorated
        return ctx
