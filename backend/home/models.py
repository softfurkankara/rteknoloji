"""
Module: home.models.py
Description:

Created by: Furkan (FK) Kara
Creation Date: 2025-07-28

Developers:
    - Furkan (FK) Kara
    - Omer Faruk (OFO) Ozyurt

Notes:
    IMPORTANT:
    If you are not one of the developers listed above, please consult with them
    before making any changes to this module.
    This helps ensure that any modifications align with the module's intended
    design and use cases.

Changelog:
    - <Date>: <Description of significant changes>

"""

# region Imports
# region Python Imports
import logging
# endregion Python Imports

# region Django Imports
from django.db import models
from django.utils.text import slugify
from django.contrib.sitemaps import Sitemap
from django.utils.translation import gettext_lazy as _
# endregion Django Imports

# region ThirdParty Imports
from wagtail.blocks import (
    StructBlock, TextBlock, URLBlock,
    CharBlock, RichTextBlock, ListBlock,
    StreamBlock, IntegerBlock, DateBlock,
    PageChooserBlock
)
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting

# endregion ThirdParty Imports

# region Dev Imports
from pofo.blocks import (
    # region Home Blocks
    # region Classic
    # region Corporate
    HomeClassicCorporateSlidersBlock,
    HomeClassicCorporateAboutBlock,
    HomeClassicCorporateServicesWIconBlock,
    HomeClassicCorporateFeaturePairsBlock,
    HomeClassicCorporatePortfolioBlock,
    HomeClassicOnePageAccordionBlock,
    HomeClassicCorporateInformationBlock,
    HomeClassicCorporateParallaxFeatureBlock,
    HomeClassicCorporateServicesGalleryBlock,
    HomeClassicCorporateParallaxBlock,
    HomeClassicCorporateServicesWFeaturesBlock,
    # endregion Corporate
    # region One Page
    # endregion One Page
    # region Start Up
    HomeClassicStartUpInformationBlock,
    # endregion Start Up
    # endregion Classic
    # region Creative
    # region Small Business
    HomeCreativeSmallBusinessServicesBlock,
    HomeCreativeSmallBusinessClientsBlock,
    # endregion Small Business
    # endregion Creative
    # endregion Home Blocks
)

# endregion Dev Imports

# endregion Imports

logger = logging.getLogger(__name__)


class ExternaLinkBlock(StructBlock):
    external_link = URLBlock(
        required=False,
        help_text=_('Enter the external link')
    )
    link_text = CharBlock(
        required=True,
        help_text=_('Enter the link text')
    )


class InternalLinkBlock(StructBlock):
    internal_link = PageChooserBlock(
        required=False,
        help_text=_('Enter the internal link')
    )
    link_text = CharBlock(
        required=True,
        help_text=_('Enter the link text')
    )


class LinkBlock(StreamBlock):
    external_link = ExternaLinkBlock()
    internal_link = InternalLinkBlock()

    class Meta:
        label = _('Link')
        icon = 'link'


# region StructBlock
class FeaturesBoxItemBlock(StructBlock):
    icon = CharBlock(max_length=255)
    title = CharBlock(max_length=255)
    description = RichTextBlock()


class AboutSectionBlock(StructBlock):
    features_items = ListBlock(
        FeaturesBoxItemBlock(),
        label=_("Feature items"),
        icon="list-ul",
        required=False,
    )


class ClassicAboutSectionBlock(StructBlock):
    background_image = ImageChooserBlock(
        required=False,
        help_text=_('Banner Image can be 1950x750 px')
    )
    heading_spacer = CharBlock(max_length=255, help_text="Heading text with spacing",
                               default="Easy way to build perfect websites")
    main_heading = CharBlock(max_length=255, help_text="Main heading",
                             default="Beautifully handcrafted templates for your website")
    paragraph = RichTextBlock(help_text="Description paragraph")
    features_items = ListBlock(
        FeaturesBoxItemBlock(),
        label=_("Feature items"),
        icon="list-ul",
        required=False,
    )


class ServicesSectionBlock(StructBlock):
    heading = CharBlock(max_length=255, help_text="Heading",
                        default="Beautiful and easy to use UI, professional animations and drag & drop feature")
    paragraph = RichTextBlock(help_text="Description paragraph")
    features_items = ListBlock(
        FeaturesBoxItemBlock(),
        label=_("Feature items"),
        icon="list-ul",
        required=False,
    )


class GridImageItemBlock(StructBlock):
    image = ImageChooserBlock(
        required=False,
        help_text=_('Image can be 1950x750 px')
    )
    alt_text = CharBlock(
        required=False,
        max_length=255,
        help_text=_("Image alt text (SEO)."),
    )

    class Meta:
        icon = "image"
        label = _("Image Column")


class GridContentItemBlock(StructBlock):
    """
    Single text column (heading, sub-heading, paragraph, button).
    """

    eyebrow = CharBlock(
        required=False,
        max_length=255,
        help_text=_("Small top label (e.g. “Build perfect websites”)."),
    )
    heading = CharBlock(
        required=True,
        max_length=255,
        help_text=_("Main heading text."),
    )
    paragraph = RichTextBlock(
        required=True,
        help_text=_("Supporting paragraph text."),
    )
    button_text = CharBlock(
        required=False,
        max_length=50,
        default="Read More",
    )
    button_link = URLBlock(
        required=False,
        help_text=_("Call-to-action link URL."),
    )

    class Meta:
        icon = "doc-full"
        label = _("Content Column")


class ImageTextGridSectionBlock(StructBlock):
    """
    Four-column “image | text | image | text” section.
    The order of blocks defines the layout; default mirrors provided HTML.
    """

    columns = StreamBlock(
        [
            ("image_item", GridImageItemBlock()),
            ("content_item", GridContentItemBlock()),
        ],
        min_num=4,
        max_num=4,
        help_text=_("Exactly four items: image, text, image, text."),
    )

    class Meta:
        icon = "placeholder"
        label = _("Image/Text Grid Section")


class CategoryBlock(StructBlock):
    """
    Free-form category:
      • slug → .web, .branding (CSS class, boşluk veya Türkçe karakter yok)
      • label → Nav’da görünen metin
    """
    slug = CharBlock(
        max_length=40,
        help_text=_("Slug used as CSS class, e.g. “web”"),
    )
    label = CharBlock(
        max_length=40,
        help_text=_("Label shown in filter nav, e.g. “Web”"),
    )

    class Meta:
        icon = "tag"
        label = _("Category")


class PortfolioItemBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    title = CharBlock(max_length=120)
    subtitle = CharBlock(max_length=200, required=False)
    categories = ListBlock(CategoryBlock(), help_text=_("Add one or more categories"))
    detail_link = URLBlock(required=False)

    class Meta:
        icon = "image"
        label = _("Portfolio Item")


class PortfolioSectionBlock(StructBlock):
    nav_title = CharBlock(
        required=False,
        max_length=120,
        default="Our Works",
    )
    sub_title = CharBlock(
        required=False,
        max_length=200,
        default="Showcasing our latest works",
    )
    portfolio_items = StreamBlock(
        [("portfolio_item", PortfolioItemBlock())],
        min_num=1,
    )

    class Meta:
        icon = "grip"
        label = _("Portfolio / Filterable Grid Section")


class BulletItemBlock(CharBlock):
    class Meta:
        icon = "list-ul"
        label = _("Bullet Item")


class InfoSectionBlock(StructBlock):
    """
    Two-column “information” section:
      • Left: heading, bullet list, CTA button
      • Right: illustrative image
    """

    heading = CharBlock(
        max_length=255,
        help_text=_("Main heading text"),
        default="Beautifully handcrafted templates for your website",
    )

    bullets = ListBlock(
        BulletItemBlock(),
        help_text=_("Add bullet list items"),
        min_num=1,
    )

    button_text = CharBlock(
        max_length=50,
        required=False,
        default="ALL advantages",
    )
    button_link = URLBlock(
        required=False,
        help_text=_("URL for the call-to-action button"),
    )

    image = ImageChooserBlock(
        required=True,
        help_text=_("Right-side illustration (e.g. 1000×800px PNG)"),
    )

    class Meta:
        icon = "info"
        label = _("Information Section")


class BulletLineBlock(CharBlock):
    """Tek madde satırı."""

    class Meta:
        icon = "arrow-right"
        label = _("Bullet")


class ParallaxInfoSectionBlock(StructBlock):
    """
    Arka planda parallax görsel + sol ana görsel + sağ metin/buton.
    """

    background_image = ImageChooserBlock(
        help_text=_("Full-width parallax background (1920×1200 önerilir)"),
    )
    parallax_ratio = CharBlock(
        required=False,
        max_length=4,
        default="0.6",
        help_text=_('data-parallax-background-ratio değeri (örn. "0.6")'),
    )
    overlay_color = CharBlock(
        required=False,
        max_length=30,
        default="bg-extra-dark-gray",
        help_text=_('Opacity div’ine verilecek sınıf (örn. "bg-extra-dark-gray")'),
    )
    overlay_opacity_class = CharBlock(
        required=False,
        max_length=30,
        default="opacity-medium",
        help_text=_('Opacity yoğunluğu sınıfı (örn. "opacity-medium")'),
    )

    left_image = ImageChooserBlock(
        help_text=_("Sol taraftaki illüstrasyon (ör. PNG, genişlik ~900px)"),
    )

    heading = CharBlock(
        max_length=255,
        default="Unique, truly responsive and functional websites",
    )
    paragraph = RichTextBlock(
        default="Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    )
    bullet_list = ListBlock(
        BulletLineBlock(),
        help_text=_("Madde satırları"),
    )
    button_text = CharBlock(
        max_length=40,
        default="GET TO KNOW US",
    )
    button_link = URLBlock(
        required=False,
        help_text=_("Buton URL"),
    )

    class Meta:
        icon = "image"
        label = _("Parallax Info Section")


class FeatureMiniBlock(StructBlock):
    """Alttaki üçlü kutulardan biri."""
    icon_class = CharBlock(
        max_length=120,
        help_text=_('Icon CSS class, e.g. "icon-desktop"'),
    )
    title = CharBlock(
        max_length=120,
        default="Modern Framework",
    )
    description = RichTextBlock(
        required=True,
        default="Lorem Ipsum is simply text the printing and typesetting standard industry.",
    )

    class Meta:
        icon = "tick"
        label = _("Mini Feature")


class MasonryPortfolioSection(StructBlock):
    """
    • Sol: tek görsel
    • Sağ: üst label + heading + paragraf + buton
    • Alt satır: 3 (veya daha fazla) FeatureMiniBlock
    """

    left_image = ImageChooserBlock(
        help_text=_("Left column image (900×650 px önerilir)"),
    )

    heading = CharBlock(
        max_length=255,
        default="Responsive, convenient and multipurpose theme",
    )
    paragraph = RichTextBlock(
        default="Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    )

    button_text = CharBlock(
        max_length=40,
        default="About Company",
    )
    button_link = URLBlock(
        required=False,
    )
    right_image = ImageChooserBlock(
        help_text=_("Right column image (900×650 px önerilir)"),
    )

    class Meta:
        icon = "snippet"
        label = _("MasonryPortfolioSection")


class CounterItemBlock(StructBlock):
    """
    Tek sayaç kutusu.
    """
    icon_class = CharBlock(
        max_length=120,
        help_text=_('İkon CSS sınıfı, ör. "icon-desktop"'),
    )
    number = IntegerBlock(
        min_value=0,
        default=350,
        help_text=_("Sayaçta gösterilecek sayı"),
    )
    label = CharBlock(
        max_length=80,
        default="Happy Clients",
    )

    class Meta:
        icon = "plus"
        label = _("Counter Item")


class CounterSectionBlock(StructBlock):
    """
    Tam sayaç bölümü – sınırsız CounterItemBlock listesi.
    """
    items = ListBlock(
        CounterItemBlock(),
        min_num=1,
        help_text=_("Sayaç öğeleri ekleyin"),
    )

    class Meta:
        icon = "pilcrow"
        label = _("Counters Section")


class ClientLogoBlock(StructBlock):
    """
    Tek logo + link.
    """
    logo = ImageChooserBlock(required=True)
    company_name = CharBlock(max_length=120, default="Company Name")
    work_description = CharBlock(max_length=220, default="Work Description", required=False)
    link = URLBlock(required=False, help_text=_("Logo tıklandığında gidilecek URL"))

    class Meta:
        icon = "link"
        label = _("Client Logo")


class ClientsSliderSectionBlock(StructBlock):
    """
    Swiper.js kullanan logo slider bölümü.
    """
    logos = ListBlock(
        ClientLogoBlock(),
        min_num=1,
        help_text=_("Slider’a eklenecek logolar"),
    )

    class Meta:
        icon = "site"
        label = _("Clients Slider Section")


class BlogCardBlock(StructBlock):
    """
    Tek blog kartı (görsel + meta + link).
    """
    image = ImageChooserBlock(required=True)
    published_date = DateBlock(
        help_text=_("Yayın tarihi"),
    )
    author_name = CharBlock(max_length=60, default="John Doe")
    author_url = URLBlock(required=False)
    title = CharBlock(max_length=120, default="Post title")
    post_link = URLBlock(required=True)
    excerpt = RichTextBlock(
        max_length=220,
        features=["bold", "italic", "link"],
        required=False,
        help_text=_("Kısa özet (en fazla 220 karakter)"),
    )

    class Meta:
        icon = "doc-full"
        label = _("Blog Card")


class LatestBlogSectionBlock(StructBlock):
    """
    Üst başlık + dinamik blog kartları (Masonry grid).
    """
    small_label = CharBlock(
        max_length=120, default="Publish what you think"
    )
    heading = CharBlock(
        max_length=120, default="Latest Blogs"
    )
    posts = ListBlock(
        BlogCardBlock(),
        min_num=1,
        help_text=_("Gösterilecek blog yazıları"),
    )

    class Meta:
        icon = "list-ul"
        label = _("Latest Blog Section")


# endregion StructBlock

@register_snippet
class SocialMediaPlatform(models.Model):
    class SocialMediaIcon(models.TextChoices):
        INSTAGRAM = 'fa-brands fa-instagram', 'instagram'
        FACEBOOK = 'fa-brands fa-facebook-f', 'facebook'
        TWITTER = 'fa-brands fa-x-twitter', 'x'
        YOUTUBE = 'fa-brands fa-youtube', 'youtube'
        WHATSAPP = 'fa-brands fa-whatsapp', 'whatsapp'

    name = models.CharField(_("Platform name"), max_length=50)
    icon = models.CharField(
        _('Icon'),
        choices=SocialMediaIcon.choices,
        null=True,
        blank=True
    )
    url = models.URLField(_("URL"), null=True, blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
        FieldPanel('url'),
    ]

    class Meta:
        verbose_name = _("Social Media Platform")
        verbose_name_plural = _("Social Media Platforms")

    def __str__(self):
        return self.name


class HomePage(Page):
    max_count = 1
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',

    )
    body = StreamField([
        # region Home Classic Corporate
        ("home_classic_corporate_sliders", HomeClassicCorporateSlidersBlock()),
        ("home_classic_corporate_about", HomeClassicCorporateAboutBlock()),
        ("home_classic_corporate_services_wicon", HomeClassicCorporateServicesWIconBlock()),
        ("home_classic_corporate_feature_pairs", HomeClassicCorporateFeaturePairsBlock()),
        ("home_classic_corporate_portfolio", HomeClassicCorporatePortfolioBlock()),
        ("home_classic_corporate_information", HomeClassicCorporateInformationBlock()),
        ("home_classic_corporate_parallax_feature", HomeClassicCorporateParallaxFeatureBlock()),
        ("home_classic_corporate_services_gallery", HomeClassicCorporateServicesGalleryBlock()),
        ("home_classic_corporate_parallax", HomeClassicCorporateParallaxBlock()),
        ("home_classic_corporate_services_wfeatures", HomeClassicCorporateServicesWFeaturesBlock()),
        # endregion Home Classic Corporate
        # region Home Classic Corparate
        ('home_about_section', ClassicAboutSectionBlock()),
        ('about_section', AboutSectionBlock()),
        ("masonry_portfolio_section", MasonryPortfolioSection()),
        ("counter_section", CounterSectionBlock()),
        ("parallax_info_section", ParallaxInfoSectionBlock()),
        ("clients_slider_section", ClientsSliderSectionBlock()),
        ("latest_blog_section", LatestBlogSectionBlock()),
        ("home_classic_one_page_accordion", HomeClassicOnePageAccordionBlock()),
        ("home_classic_start_up_information", HomeClassicStartUpInformationBlock()),
        ("home_creative_small_business_services", HomeCreativeSmallBusinessServicesBlock()),
        ("home_creative_small_business_clients", HomeCreativeSmallBusinessClientsBlock()),

    ])
    content_panels = Page.content_panels + [
        FieldPanel('logo'),
        FieldPanel('body'),
        InlinePanel(
            'home_in_pages',
            label='Home In Pages',
        )
    ]


class HomeInPages(Orderable):
    home_page = ParentalKey(
        'home.HomePage',
        related_name='home_in_pages',
        on_delete=models.CASCADE,
    )
    showcase = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        PageChooserPanel('showcase', [
            'home.EmptyPage', ]),
    ]


class ContactAddressBlock(StructBlock):
    icon = CharBlock(max_length=120, default="icon-map text-deep-pink icon-medium margin-25px-bottom")
    address = ListBlock(RichTextBlock(
        null=True,
        blank=True,
    ))


class ContactPhoneBlock(StructBlock):
    icon = CharBlock(
        max_length=120,
        default="icon-phone text-deep-pink icon-medium margin-25px-bottom",
    )
    phone = ListBlock(RichTextBlock(
        null=True,
    ))


class ContactEmailBlock(StructBlock):
    icon = CharBlock(
        max_length=120,
        default="icon-mail text-deep-pink icon-medium margin-25px-bottom"
    )
    email = ListBlock(RichTextBlock(
        null=True,
    ))


class ContactWorkingHoursBlock(StructBlock):
    icon = CharBlock(
        max_length=120,
        default="icon-clock text-deep-pink icon-medium margin-25px-bottom",
    )
    working_hours = ListBlock(RichTextBlock())


class ContactHelpSection(StructBlock):
    title = CharBlock(max_length=120, default="Help us")
    subtitle = CharBlock(max_length=120, default="We are here to help")
    paragraph = RichTextBlock(
        null=True,
        blank=True,
        features=["bold", "italic", "link"],
        help_text=_('Enter the description of the Page')
    )


class ContactSectionBlock(StructBlock):
    contact_help_section = ContactHelpSection(rquired=False)
    contact_image = ImageChooserBlock(required=False)
    contact_video = URLBlock(required=False)  # silinecek.
    contact_address = ListBlock(ContactAddressBlock(), required=False)
    contact_phone = ListBlock(ContactPhoneBlock(), required=False)
    contact_email = ListBlock(ContactEmailBlock(), required=False)
    contact_working_hours = ListBlock(ContactWorkingHoursBlock(), required=False)
    descripton = RichTextField(
        null=True,
        blank=True,
        features=["bold", "italic", "link"],
        help_text=_('Enter the description of the Page')
    )


class BlogMediaBlock(StructBlock):
    image = ImageChooserBlock(required=False, help_text="Tekil bir görsel ekleyin.")
    video = URLBlock(required=False, help_text="Video URL'si (YouTube, Vimeo vb.)")
    slider = ListBlock(ImageChooserBlock(required=False), required=False,
                       help_text="Slider için birden fazla görsel ekleyin.")
    gallery = ListBlock(ImageChooserBlock(required=False), required=False,
                        help_text="Galeri için birden fazla görsel ekleyin.")

    class Meta:
        icon = "media"
        label = "Blog Medya"


class BlogSectionBlock(StructBlock):
    blog_media = ListBlock(BlogMediaBlock(), required=False, help_text="Bir veya birden fazla medya bloğu ekleyin.")
    description = RichTextBlock(
        required=False,
        features=["bold", "italic", "link"],
        help_text="Blog içeriğini buraya girin."
    )

    class Meta:
        icon = "doc-full"
        label = "Blog Bölümü"


class HeroSectionBlock(StructBlock):
    title = CharBlock(required=True, help_text="Ana başlık (örn: Gücünü Deneyimden Alan Çözümler)")
    subtitle = TextBlock(required=False,
                         help_text="Alt açıklama / slogan (örn: Yılların tecrübesini, yenilikçi bakış açısıyla birleştiriyoruz.)")


class CompanyProfileBlock(StructBlock):
    company_manager = CharBlock(required=False, help_text="Firma Yöneticisi  Ad Soyad")
    manager_title = CharBlock(required=False, help_text="Ünvan")
    manager_jobs = CharBlock(required=False, help_text="Meslek")
    image = ImageChooserBlock(required=False, help_text="Firma görseli")
    description = RichTextBlock(required=True, features=["bold", "italic", "link"],
                                help_text="Firma profili açıklaması")


class VisionMissionBlock(StructBlock):
    vision = TextBlock(required=True, help_text="Vizyon açıklaması")
    mission = TextBlock(required=True, help_text="Misyon açıklaması")


class ValueItemBlock(StructBlock):
    icon_class = CharBlock(required=True, help_text="İkon CSS sınıfı (örn: icon-shield, icon-lightbulb)")
    title = CharBlock(required=True, help_text="Değerin başlığı (örn: Deneyim ve Güven)")
    description = TextBlock(required=True, help_text="Değerin kısa açıklaması")


class ValuesBlock(StructBlock):
    items = ListBlock(ValueItemBlock(), help_text="Değerleri ekleyin (ikon + başlık + açıklama)")


class AboutUsSectionBlock(StructBlock):
    hero_section = HeroSectionBlock()
    company_profile = CompanyProfileBlock()
    vision_mission = VisionMissionBlock()
    values = ValuesBlock()

    class Meta:
        icon = "user"
        label = "Hakkımızda Bölümü"


class EmptyPage(Page):
    parent_page_types = [
        'home.HomePage',
        'home.EmptyPage'
    ]
    subpage_types = [
        'home.EmptyPage'
    ]
    # thumbnail_image
    thumbnail_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = RichTextField(
        null=True,
        blank=True,
        features=["bold", "italic", "link"],
        help_text=_('Enter the description of the Page')
    )
    in_sitemap = models.BooleanField(default=True)
    in_sidebar = models.BooleanField(default=False)
    body = StreamField([
        ('blog_section', BlogSectionBlock()),
        ('contact_section', ContactSectionBlock()),
        ('about_us_section', AboutUsSectionBlock()),
        ("clients_slider_section", ClientsSliderSectionBlock()),
    ], null=True,
        blank=True,
        use_json_field=True,
        help_text=_('The body of the page.'))
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('thumbnail_image'),
        FieldPanel('description'),
        InlinePanel(
            'empty_in_pages',
            label='Empty In Pages',
        )
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('in_sitemap'),
        FieldPanel('in_sidebar')
    ]

    def save(self, *args, **kwargs):
        tr_map = str.maketrans({
            'ç': 'c', 'Ç': 'C',
            'ğ': 'g', 'Ğ': 'G',
            'ı': 'i', 'İ': 'I',
            'ö': 'o', 'Ö': 'O',
            'ş': 's', 'Ş': 'S',
            'ü': 'u', 'Ü': 'U'
        })
        if self.title and (not self.slug or any(ch in "çğıöşüÇĞİÖŞÜ" for ch in self.slug)):
            clean_title = self.title.translate(tr_map)
            self.slug = slugify(clean_title)

        super().save(*args, **kwargs)

    def get_template(self, request, *args, **kwargs):
        if self.get_children().exists():
            return 'home/empty_index.html'
        else:
            return 'home/empty_page.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        from .forms import ProjectContactForm
        context['sidebar_categories'] = (
            self.get_parent().get_children().live().order_by('-first_published_at')[:16]
        )
        context['form'] = ProjectContactForm()
        return context


class EmptyPageInPages(Orderable):
    home_page = ParentalKey(
        'home.EmptyPage',
        related_name='empty_in_pages',
        on_delete=models.CASCADE,
    )
    showcase = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        PageChooserPanel('showcase', [
            'home.EmptyPage', ]),
    ]


class ProjectContact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    company_name = models.CharField(
        max_length=255,
        verbose_name="Firma Adı",
        blank=True,
        null=True,
    )
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon")
    email = models.EmailField(verbose_name="E-posta")
    comment = models.TextField(verbose_name="Proje Açıklaması", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proje İletişim"
        verbose_name_plural = "Proje İletişim Talepleri"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"


@register_setting
class RobotsTxtSettings(BaseSiteSetting):
    content = models.TextField(
        verbose_name="robots.txt İçeriği",
        help_text="robots.txt içeriğini buradan düzenleyebilirsin."
    )

    panels = [
        FieldPanel("content"),
    ]


class WagtailPageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return [
            page for page in Page.objects.live().public().specific()
            if page.get_url(request=None) is not None
        ]

    def location(self, obj):
        url = obj.get_url(request=None)
        return url if url else ""

    def lastmod(self, obj):
        return obj.last_published_at
