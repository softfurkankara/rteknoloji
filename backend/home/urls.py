from django.urls import path
from .views import project_contact_view

app_name = 'home'
urlpatterns = [
    path('contact-project/', project_contact_view, name='project-contact'),
]
