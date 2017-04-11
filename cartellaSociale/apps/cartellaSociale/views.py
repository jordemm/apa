from django.views.generic import DetailView
from django.views.generic.base import View
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Utenti, Visite
from django.http import HttpResponse
from django.shortcuts import redirect, Http404
from django.http import JsonResponse
from .forms import VisiteAmbulatorioForm

from .utils import render_to_pdf
import datetime
from .codice_fiscale.codice_fiscale import calcola

def index(request):
    return redirect('/admin')

def codice_fiscale_ajax(request):
    # print('____________in view__________________')
    # print(cf)
    nome = request.GET.get('nome').lower()
    cognome = request.GET.get('cognome').lower()
    data = request.GET.get('nasc').lower()
    sesso = request.GET.get('sesso').lower()
    comune = request.GET.get('comune').lower()


    if request.is_ajax():
        print(request.GET)
        data = {'cf': calcola(cognome=cognome, nome=nome, sesso=sesso, data=data, comune=comune)}
        return JsonResponse(data)
    else:
        raise Http404

class GenerateUtentiPdf(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GenerateUtentiPdf, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        visite_id = request.GET.get('visite')
        tutti = request.GET.get('tutti')

        try:
            utente = Utenti.objects.get(pk=pk)
            if tutti:
                visite = Visite.objects.filter(id_ut=utente)
            else:
                visite = Visite.objects.filter(pk=visite_id)

            data = {
               'utente': utente,
               'visite': visite,
            }

        except:
            data = {
                'utente': None,
            }

        pdf = render_to_pdf('pdf/report_utenti.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class ComunicazioneAmmissionePdf(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ComunicazioneAmmissionePdf, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = {
                'utente': Utenti.objects.get(pk=pk),
                'today': datetime.datetime.today()
            }
        except:
            data = {
                'utente': None,
            }

        pdf = render_to_pdf('pdf/communicazione_ammissione.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class ComunicazioneDimmissionePdf(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ComunicazioneDimmissionePdf, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = {
                'utente': Utenti.objects.get(pk=pk),
                'today': datetime.datetime.today()
            }
        except:
            data = {
                'utente': None,
            }

        pdf = render_to_pdf('pdf/communicazione_dimmissione.html', data)
        return HttpResponse(pdf, content_type='application/pdf')