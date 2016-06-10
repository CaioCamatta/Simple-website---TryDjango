from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact/$', views.home, name='home'),
    url(r'^$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
]