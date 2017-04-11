"""cartellaSociale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from cartellaSociale.apps.cartellaSociale.views import index, GenerateUtentiPdf, ComunicazioneAmmissionePdf, ComunicazioneDimmissionePdf, codice_fiscale_ajax


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^codice_f/$', codice_fiscale_ajax, name='codice_fiscale'),
    url(r'^utente/(?P<pk>\d+)/comunicazione_ammissione.pdf$', ComunicazioneAmmissionePdf.as_view(), name='comunicazione_ammissione_pdf'),
    url(r'^utente/(?P<pk>\d+)/comunicazione_dimmissione.pdf$', ComunicazioneDimmissionePdf.as_view(), name='comunicazione_dimmissione_pdf'),
    url(r'^utente/(?P<pk>\d+)/visite.pdf$', GenerateUtentiPdf.as_view(), name='utente_pdf'),
    # url(r'^admin/stampa-pdf/', PdfStampa.as_view(), name='stampa'),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

