from django.contrib import admin
from django.template.response import TemplateResponse
from django.conf.urls import url
from .models import Utenti, Uds, Ut, Visite, Giurisprud, Malattie, Avvocati, Magazz, Interventi, Risorse, Donazioni
from .forms import VisiteAmbulatorioForm

class UdsStackedInline(admin.StackedInline):
    # classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-closed',)
    # sortable_field_name = 'luogo'

    model = Uds
    extra = 0
    fields = [("data", 'ora', 'luogo', 'condizioni')]

class UdsTabularInline(admin.TabularInline):
    # classes = ('grp-collapse grp-close',)
    model = Uds
    extra = 0
    fields = ['luogo', 'condizioni']

class UtTabularInline(admin.TabularInline):
    classes = ('grp-collapse grp-closed',)
    model = Ut
    extra = 1
    fields = [('oggi', 'mensa', 'no_tex', 'tex_scad', 'docce', 'maga', 'pranzo', 'indum')]

class VisiteTabularInline(admin.TabularInline):
    classes = ('grp-collapse grp-closed',)
    model = Visite
    extra = 0
    fields = [('data', 'patologie', 'terapia')]

class AvvocatiTabularInline(admin.TabularInline):
    classes = ('grp-collapse grp-closed',)
    model = Avvocati
    extra = 0
    fields = [('data', 'id', 'problema', 'soluzione')]

class MagazzTabularInline(admin.TabularInline):
    classes = ('grp-collapse grp-closed',)
    model = Magazz
    extra = 0
    fields = [('data', 'settore', 'data_fine')]


class AccoglienzaResidenzialeAdmin(admin.ModelAdmin):
    change_form_template = 'accoglienza_residenziale_change_form.html'
    # change_list_template = "admin/change_list_filter_sidebar.html"
    # change_list_filter_template = "admin/filter_listing.html"

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Customize this title.'}
        return super(AccoglienzaResidenzialeAdmin, self).changelist_view(request, extra_context=extra_context)

    fields = (
        [
                ('cogn', 'nom', 'liv01_accesso','liv01_servizio'),
                ('liv01_motivo', 'liv04_dormit', 'liv04_servizio', 'liv04_tipologia'),
                ('liv04_allprov', 'liv04_statusacc', 'liv04_amm', 'liv04_dimmprev'),
                ('liv04_acccoll', 'liv04_acccoll_dal', 'liv04_acccoll_al'),
                ('liv04_profilo'),
                ('liv04_conddimm', 'liv04_motdimm')
    ]


        # ('another collapsable fieldset', {
        #     'classes': ('grp-collapse grp-closed',),
        #     'fields': ('nom', 'foto', 'nasc', 'cf',),
        # }),
        # ('Uds Inline', {
        #     'classes': ('placeholder luogo',),
        #     'fields': ('luogo')
        # }),
    )
    list_display = [
        'nom', 'cogn', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv04_statusacc',
        'liv04_tipologia', 'liv04_allprov', 'liv04_acccoll', 'liv04_acccoll_dal', 'liv04_acccoll_al'
    ]
    search_fields = ('nom', 'cogn')
    list_filter = ['liv01_servizio', 'liv04_statusacc', 'liv01_motivo', 'liv04_tipologia']
    # inlines = [UdsTabularInline]


class CartellaSocialeAdmin(admin.ModelAdmin):
    change_form_template = 'cartella_sociale_change_form.html'
    view_on_site = True
    save_on_top = True

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra = extra_context or {}
        print('i********************* in change view.....')
        utente = Utenti.objects.get(pk=object_id)
        visite_queryset = Visite.objects.filter(id_ut=utente)
        extra['visite'] = visite_queryset
        extra['form'] = VisiteAmbulatorioForm()
        extra['form'].fields['visite'].queryset = visite_queryset
        return super(CartellaSocialeAdmin, self).change_view(request, object_id,
                                                     form_url, extra_context=extra)
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Customize this title.'}
        return super(CartellaSocialeAdmin, self).changelist_view(request, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        print('------------------------', form.cleaned_data['nasc'])
        # obj.cf = 'newcodicefiscale'
        obj.save()

    fieldsets = (
        ('', {
            'fields':(
                ('image_tag', 'foto'),
                ('anno', 'oggi', 'del_field', 'ai'),
                ('cittadinanza', 'liv04_dormit', 'cogn', 'nom'),
                ('genere', 'nasc', 'luogo','paese'),
                ('status', 'cf', 'telef'),
                ( 'doc', 'ndoc', 'scadenza'),
                ('tipologia_pds', 'res', 'resultima', 'domicilio'),
                ( 'homeless', 'homelesstip', 'tessmensa', 'scadtessmen'),
                ('richiesta', 'orinetamento', 'ind')
            ),
        }),
        ('SEZIONE TUTELA SALUTE', {
            'classes': ('grp-collapse grp-closed',),
            'fields':(
                ('ssn', 'ssntess', 'ssnscad'),
                ('pass_field', 'esenz', 'esenznum'),
                ('stp', 'stpnum', 'stpscad' ),
                ('medicobase', 'medicobasenom', 'medicobasetel'),
                ('salutement', 'salutementop', 'salutementtel'),
                ('sert', 'sertop', 'serttel'),
            )
        }),
    )
    readonly_fields = ('image_tag',)
    list_display = [
        'nom', 'cogn', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv04_statusacc',
        'liv04_tipologia', 'liv04_allprov', 'liv04_acccoll', 'liv04_acccoll_dal', 'liv04_acccoll_al'
    ]
    search_fields = ('nom', 'cogn')
    list_filter = ['liv01_servizio', 'liv04_statusacc', 'liv01_motivo', 'liv04_tipologia', 'ind']
    inlines = [UtTabularInline, VisiteTabularInline]


class CartellaSocialeAvvocatiAdmin(admin.ModelAdmin):
    change_form_template = 'cartella_sociale_avvocati_change_form.html'

    # change_form_template = 'custom_change_form.html'
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Customize this title.'}
        return super(CartellaSocialeAvvocatiAdmin, self).changelist_view(request, extra_context=extra_context)

    fieldsets = (
        ('', {
            'fields':(
                ('anno', 'oggi', 'del_field', 'cittadinanza'),
                ('cogn', 'nom', 'genere',),
                ( 'nasc', 'luogo','paese','status'),
                ('cf', 'telef', 'doc'),
                ('scadenza', 'ndoc', 'tipologia_pds'),
                ('res', 'resultima', 'domicilio'),
                ('homeless', 'homelesstip', 'tessmensa', 'scadtessmen', ),
                ('richiesta', 'orinetamento')
            ),
        }),
        ('SEZIONE TUTELA SALUTE', {
            'classes': ('grp-collapse grp-closed',),
            'fields':(
                ('ssn', 'ssntess', 'ssnscad'),
                ('pass_field', 'esenz', 'esenznum'),
                ('stp', 'stpnum', 'stpscad' ),
                ('medicobase', 'medicobasenom', 'medicobasetel'),
                ('salutement', 'salutementop', 'salutementtel'),
                ('sert', 'sertop', 'serttel'),
            )
        }),
    )

    list_display = [
        'nom', 'cogn', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv04_statusacc',
        'liv04_tipologia', 'liv04_allprov', 'liv04_acccoll', 'liv04_acccoll_dal', 'liv04_acccoll_al'
    ]
    search_fields = ('nom', 'cogn')
    list_filter = ['liv01_servizio', 'liv04_statusacc', 'liv01_motivo', 'liv04_tipologia']
    inlines = [UtTabularInline, AvvocatiTabularInline]


class CartellaSocialePortineriaAdmin(admin.ModelAdmin):
    change_form_template = 'cartella_sociale_portineria_change_form.html'
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Customize this title.'}
        return super(CartellaSocialePortineriaAdmin, self).changelist_view(request, extra_context=extra_context)

    fieldsets = (
        ('', {
            'fields':(
                ('anno', 'oggi', 'del_field', 'cittadinanza'),
                ('cogn', 'nom', 'genere',),
                ( 'nasc', 'luogo','paese','status'),
                ('cf', 'telef', 'doc'),
                ('ndoc', 'scadenza', 'tipologia_pds'),
                ('res', 'resultima', 'domicilio', 'homeless'),
                ('homelesstip', 'tessmensa', 'scadtessmen', 'richiesta'),
                ('orinetamento')
            ),
        }),
        ('SEZIONE TUTELA SALUTE', {
            'classes': ('grp-collapse grp-closed',),
            'fields':(
                ('ssn', 'ssntess', 'ssnscad'),
                ('pass_field', 'esenz', 'esenznum'),
                ('stp', 'stpnum', 'stpscad' ),
                ('medicobase', 'medicobasenom', 'medicobasetel'),
                ('salutement', 'salutementop', 'salutementtel'),
                ('sert', 'sertop', 'serttel'),
            )
        }),
    )

    list_display = [
        'nom', 'cogn', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv04_statusacc',
        'liv04_tipologia', 'liv04_allprov', 'liv04_acccoll', 'liv04_acccoll_dal', 'liv04_acccoll_al'
    ]
    search_fields = ('nom', 'cogn')
    list_filter = ['liv01_servizio', 'liv04_statusacc', 'liv01_motivo', 'liv04_tipologia']
    inlines = [UtTabularInline, MagazzTabularInline]


class ElencoAttenzionatiAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.objects.exclude(ind=None)

    list_display = ["nom", 'cogn', 'nasc', 'luogo', 'ind']
    list_display_link = ['nom', 'cogn']
    fields = [('nom', 'cogn', 'nasc'), ('ind'), 'note']
    list_filter = ('ind', 'luogo')


class MagazzAdmin(admin.ModelAdmin):
    model = Magazz
    list_display = ['id_ut', 'data', 'settore', 'data_fine']
    list_filter = ['id_ut', 'settore']
    fields = [('id_ut', 'data', 'settore', 'data_fine')]
    # readonly_fields = [ 'id_ut']

    # def get_id_ut(self, obj):
    #     return obj.id_ut.nom+ ' '+obj.id_ut.cogn
    #
    # get_id_ut.short_description = 'Utente'
    # get_id_ut.admin_order_field = 'id_ut__nom'


class ProgettoPersonaleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': (
                ('cogn', 'nom', 'liv01_accesso' ),
                ('liv01_servizio', 'liv01_motivo', 'liv05_titolare'),
                ('liv05_refapa', 'liv05_obiett'),
                ('liv05_duratadal', 'liv05_durataal'),
            )
        }),
        ('DESCRIZIONE DEL CASO', {
            'classes': ('grp-collapse grp-open',),
            'fields': (
                ('liv05_descrcrit'), ('liv05_servapa'),
                ('liv05_descrris'), ('liv05_servaltri'),
                ('liv05_imppers')
            )
        }),
    )

    list_display = ['nom', 'cogn', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv05_duratadal', 'liv05_durataal']
    list_filter = ('liv01_accesso', 'liv01_servizio', 'liv01_motivo')
    # search_fields = ('liv01_accesso', 'liv01_accesso')


class InterventiTabularInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
    model = Interventi
    extra = 0
    fields = [('interventi', 'tempo')]


@admin.register(Visite)
class VisiteAdmin(admin.ModelAdmin):
    class Meta:
        model = Visite

    list_display = ('id_ut', 'data', 'patologie')
    search_fields = ('id_ut__nom', 'id_ut__cogn')
    list_filter = ('id_ut__nom', 'id_ut__cogn')

class ProgettoPersonaleDiarioDegliInterventiEAggiornamentoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': (
                ('cogn', 'nom', 'liv01_accesso'),
                ('liv01_servizio', 'liv01_motivo'),
            )
        }),
        ('AGGIORNAMENTO E DIARIO: DATA, RILEVAZIONE, TIPO DI INTERVENTO, SOGETTI COINVOLTI', {
            'fields': (
                ('liv05_aggiorn'),
            )
        }),
    )
    list_display = ['nom', 'cogn', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo']
    list_filter = ('liv01_accesso', 'liv01_servizio', 'liv01_motivo')
    inlines = [InterventiTabularInline]


class ProgettoPersonaleRisorseRisultati(admin.ModelAdmin):

    fieldsets = (
        ('', {
            'fields':(
                ('cogn', 'nom'),
                ('liv01_accesso', 'liv01_servizio', 'liv01_motivo'),
            )
        }),
        ('RISORSE IMPIEGATE', {
            'fields': (
                ('liv05_oretit_refapa', 'liv05_collagg', 'liv05_incontriinv'),
                ('liv05_volcoinv', 'liv05_contrapa'),
            )
        }),
        ('RISULTATI OTTENUTI', {
            'fields': (
                ('liv05_famiglia', 'liv05_lavoro'),
                ('liv05_salute', 'liv05_diritti'),
            )
        }),
        ('CONCLUSIONE DEL PROGETTO PERSONALE', {
            'fields': (
                ('liv05_conclprog'),
            )
        }),
    )

    list_display = ('cogn', 'nom', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv05_famiglia', 'liv05_lavoro', 'liv05_salute', 'liv05_diritti' )
    search_fields = ('cogn', 'nom')
    list_filter = ('liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv05_famiglia', 'liv05_lavoro', 'liv05_salute', 'liv05_diritti', 'liv05_conclprog')


class ServiziLavoroAbitazioneAdmin(admin.ModelAdmin):
    fields = (
        ('cogn', 'nom'),
        ('liv01_accesso', 'liv01_servizio', 'liv01_motivo'),
        ('liv01_operatore', 'liv01_servutilizzati'),
        ('liv01_status', 'liv01_coniuge', 'liv01_figli'),
        ('liv01_altririf'),
        ('liv01_famiglia'),
        ('liv01_abitaz', 'liv01_senzadim', 'liv01_notte'),
        ('liv01_condprof', 'liv01_reddito', 'liv01_reddliv'),
        ('liv01_ultimolavoro', 'liv01_tipologia', 'liv01_azienda'),
        ('liv01_formprofdescr', 'livo01_italiano', 'liv01_pat', 'liv01_ci'),
        ('liv01_tititaliano', 'liv01_titstran'),
        ('liv01_suss', 'liv01_pens')
    )

    list_display = ('cogn', 'nom', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv01_status', 'liv01_abitaz', 'liv01_senzadim')
    search_fields = ('cogn', 'nom')
    list_filter = ('liv01_accesso', 'liv01_servizio', 'liv01_motivo', 'liv01_abitaz', 'liv01_tipologia')


class TutelaDeiDirittiAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': (
                ('cogn', 'nom'),
                ('liv01_accesso', 'liv01_servizio', 'liv01_motivo'),
                ('liv03_req', 'liv03_avvoc')
            )
        }),
        ('PROBLEMATICA RISOLUZIONE', {
            'fields': (
                ('liv03_note'),
            )
        })
    )

    list_display = ('cogn', 'nom', 'liv01_accesso', 'liv01_servizio', 'liv01_motivo')
    search_fields = ('cogn', 'nom', 'liv03_avvoc')
    list_filter = ('liv01_accesso', 'liv01_servizio', 'liv01_motivo')


def create_modeladmin(modeladmin, model, name=None, ver_nam_plu=None):
    class Meta:
        proxy = True
        app_label = model._meta.app_label
        verbose_name_plural = ver_nam_plu

    attrs = {'__module__': '', 'Meta': Meta, }
    newmodel = type(name, (model,), attrs)
    admin.site.register(newmodel, modeladmin)
    return modeladmin


create_modeladmin(AccoglienzaResidenzialeAdmin, name='Accoglienza Residenziale', model=Utenti, ver_nam_plu='Accoglienze Residenziali')
create_modeladmin(CartellaSocialeAdmin, name='Cartella Sociale', model=Utenti, ver_nam_plu='Cartelle Sociali')
create_modeladmin(CartellaSocialeAvvocatiAdmin, name='Cartella Sociale Avvocato', model=Utenti, ver_nam_plu='Cartelle Sociale Avvocati')
create_modeladmin(CartellaSocialePortineriaAdmin, name='Cartella Sociale Portineria', model=Utenti, ver_nam_plu='Cartelle Sociale Portineria')
create_modeladmin(ElencoAttenzionatiAdmin, name='Elenco Attenzionati', model=Utenti, ver_nam_plu='Elenchi Attenzionati')
create_modeladmin(MagazzAdmin, name='Magazzi', model=Magazz, ver_nam_plu='Magazzi')
create_modeladmin(ProgettoPersonaleAdmin, name='Progetto personale', model=Utenti, ver_nam_plu='Progetti personale')
create_modeladmin(ProgettoPersonaleDiarioDegliInterventiEAggiornamentoAdmin, name='Progetto personale Interventi', model=Utenti, ver_nam_plu='Progetti personale Interventi')
create_modeladmin(ProgettoPersonaleRisorseRisultati, name='progetto personale, risorse e risultati', model=Utenti, ver_nam_plu='progetti personale, risorse e risultati')
create_modeladmin(ServiziLavoroAbitazioneAdmin, name='Servizi Lavoro Abitazione', model=Utenti, ver_nam_plu='Servizi Lavoro Abitazione')
create_modeladmin(TutelaDeiDirittiAdmin, name='Tutela dei diritti', model=Utenti, ver_nam_plu='Tutela dei diritti')



@admin.register(Ut)
class UtAdmin(admin.ModelAdmin):
    class Meta:
        model = Ut

    list_display = ['id_ut', 'oggi', 'mensa', 'no_tex', 'docce', 'maga', 'pranzo', 'indum', 'tex_scad']
    list_filter = ['id_ut', 'oggi', 'mensa', 'no_tex', 'docce', 'maga', 'pranzo', 'indum', 'tex_scad']


@admin.register(Utenti)
class UtentiAdmin(admin.ModelAdmin):
    # fields = ['nom', ('cogn', 'luogo', 'anno')]
    list_display = ['id_ut', "nom", 'cogn', 'luogo']
    list_editable = ['luogo']
    list_display_links = ('id_ut', 'nom',)
    search_fields = ('anno', 'luogo')
    list_filter = ['anno', 'nom']
    list_per_page = 50
    # site_url = None

    inlines = [UdsStackedInline]

    class Meta:
        model = Utenti

@admin.register(Risorse)
class RisorseAdmin(admin.ModelAdmin):
    model = Risorse
    list_display = ('tip_risorsa', 'riferim', 'riferim_ente', 'telefono', 'mail')
    list_filter = ('tip_risorsa', 'riferim', 'riferim_ente')
    search_fields = ('riferim', 'riferim_ente')

@admin.register(Uds)
class UdsAdmin(admin.ModelAdmin):
    model = Uds

@admin.register(Magazz)
class MagazzAdmin(admin.ModelAdmin):
    model = Magazz

@admin.register(Interventi)
class InterventiAdmin(admin.ModelAdmin):
    model = Interventi

@admin.register(Donazioni)
class DonazioniAdmin(admin.ModelAdmin):
    change_form_template = 'donazioni_change_form.html'
    model = Donazioni

# @admin.register(Uds)
# class UdsAdmin(admin.ModelAdmin):
#     list_display = ["data", 'ora', 'luogo', 'condizioni']
#     list_filter = ['id_ut__cogn', 'id_ut__nom', 'data', 'ora', 'luogo']
#
#     class Meta:
#         model = Uds
@admin.register(Giurisprud)
class GiurisprudAdmin(admin.ModelAdmin):
    class Meta:
        model = Giurisprud