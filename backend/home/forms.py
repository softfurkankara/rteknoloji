from django import forms
from .models import ProjectContact
from django.conf import settings

from .services.mail import send_mail


class ProjectContactForm(forms.ModelForm):
    class Meta:
        model = ProjectContact
        fields = ['name', 'phone','company_name', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad Soyad *', 'class': 'big-input required'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon', 'class': 'big-input required'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Firma Adı', 'class': 'big-input required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail *', 'class': 'big-input required'}),
            'comment': forms.Textarea(
                attrs={'placeholder': 'Projenizi tanımlayın', 'rows': 6, 'class': 'big-textarea required'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=commit)

        subject = "İletişim Formu Hk."
        body = (
            f"Yeni İletişim Formu Dolduruldu contact form submitted.\n\n"
            f"Ad Soyad: {instance.name}\n"
            f"Telefon: {instance.phone or 'N/A'}\n"
            f"Firma Adı: {instance.company_name or 'N/A'}\n"
            f"E-Posta: {instance.email}\n"
            f"Yorum: \n{instance.comment}")
        admin_email = settings.SMTP_MANAGER_MAIL  # örnek: 'info@domain.com'
        send_mail(admin_email, subject, body)
        confirmation_subject = "Talebiniz Alındı – Rintech Roobtic"
        confirmation_body = (
            f"{instance.name},\n\n"
            f"İletişim formunuz başarıyla alınmıştır. En kısa sürede sizinle iletişime geçilecektir.\n"
            f"İlginiz için teşekkür ederiz.\n\n"
            f"Rintech Robotic Ekibi"
        )
        send_mail(instance.email, confirmation_subject, confirmation_body)
        return instance
