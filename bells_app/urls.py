from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('admission_page', views.admission_page, name='admission_page'),
    path('contact_page', views.contact_page, name='contact_page'),
]
