from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from wagtail.models import Site
from wagtail.views import serve
from django.contrib import messages
from .forms import ProjectContactForm
from .models import HomePage, RobotsTxtSettings


def wagtail_custom_404(request, exception=None):
    """
    Custom 404 error handler.
    """
    return render(request, 'home/404.html', status=404)


def wagtail_custom_500(request):
    """
    Custom 500 error handler.
    """
    return render(request, 'home/500.html', status=500)


def custom_wagtail_serve(request, path):
    try:
        return serve(request, path)
    except Http404:
        return wagtail_custom_404(request)


@require_POST
def project_contact_view(request):
    form = ProjectContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Mesajınız başarıyla gönderildi! En kısa sürede sizinle iletişime geçeceğiz.")
    else:
        messages.error(request, "Mesaj gönderilirken bir hata oluştu. Lütfen tekrar deneyin.")

    # Her durumda anasayfaya yönlendir
    homepage = HomePage.objects.first()
    if homepage:
        return redirect(homepage.url)
    return redirect('/')


def robots_txt(request):
    site = Site.find_for_request(request)
    settings_obj = RobotsTxtSettings.for_site(site)
    return HttpResponse(settings_obj.content, content_type="text/plain")
