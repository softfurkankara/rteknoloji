from wagtail.models import Page, Locale
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_sitemap_pages(context):
    request = context["request"]
    active_language = request.LANGUAGE_CODE

    try:
        # Aktif dile karşılık gelen Locale objesini bul
        active_locale = Locale.objects.get(language_code=active_language)
    except Locale.DoesNotExist:
        # Bulunamazsa varsayılan dili kullan
        active_locale = Locale.get_default()

    # Ana sayfa altındaki üst seviye sayfaları sadece o dile göre getir
    pages = (
        Page.objects.live()
        .public()
        .filter(depth__lte=3, show_in_menus=True, locale=active_locale)
        .specific()
        .order_by("path")
    )

    return pages