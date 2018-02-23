from django.conf.urls import url
from milhas.views import home, how
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
		url(r'^como-funciona$', how, name ='como-funciona'),
    	url(r'^', home, name='home')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

