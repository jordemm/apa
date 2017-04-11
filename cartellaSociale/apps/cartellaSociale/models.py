# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.utils.safestring import mark_safe
from django.core.validators import MinLengthValidator
from django.db import models
from .utils import validate_nascita
from .choices import *

def image_upload_to(instance, filename):
    return "album/%s/%s" % (instance.id_ut, filename)

class Utenti(models.Model):
    id_ut = models.AutoField(db_column='ID_ut', primary_key=True)  # Field name made lowercase.
    sicurezza = models.IntegerField(blank=True, null=True)
    del_field = models.BooleanField(db_column='del', default=False, verbose_name='record eliminato')  # Field renamed because it was a Python reserved word.
    ai = models.BooleanField(default=False, verbose_name='a.i.')
    privacy = models.IntegerField(blank=True, null=True)
    anno = models.CharField(max_length=255, blank=True, null=True)
    oggi = models.DateField(blank=True, null=True, verbose_name='data prima accoglienza')
    op = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(blank=True, null=True, upload_to=image_upload_to)
    cogn = models.CharField(max_length=255, blank=True, null=True, verbose_name='cognome')
    nom = models.CharField(max_length=255, blank=True, null=True, verbose_name='nome')
    cittadinanza = models.CharField(max_length=50, blank=True, null=True, choices=CARTELLA_SOCIALE_cittadinanza)
    genere = models.CharField(max_length=50, blank=True, null=True, choices=CARTELLA_SOCIALE_genere)
    nasc = models.DateField(blank=True, null=True, verbose_name='nato il')
    luogo = models.CharField(max_length=255, blank=True, null=True, verbose_name='citta')
    paese = models.IntegerField(blank=True, null=True, verbose_name='stato')
    status = models.CharField(max_length=255, blank=True, null=True, choices=CARTELLA_SOCIALE_status)
    cf = models.CharField(max_length=16, blank=True, null=True, validators=[MinLengthValidator(16)])
    doc = models.CharField(max_length=255, blank=True, null=True, choices=CARTELLA_SOCIALE_doc)
    ndoc = models.CharField(max_length=255, blank=True, null=True)
    scadenza = models.DateField(blank=True, null=True)
    tipologia_pds = models.CharField(db_column='tipologia pds', max_length=50, blank=True, null=True, verbose_name='pds', choices=CARTELLA_SOCIALE_tipologia_pds)  # Field renamed to remove unsuitable characters.
    res = models.BooleanField(default=False, verbose_name='residenza')
    resultima = models.CharField(max_length=50, blank=True, null=True, verbose_name='ultima residenza')
    domicilio = models.CharField(max_length=50, blank=True, null=True)
    homeless = models.BooleanField(default=False)
    homelesstip = models.CharField(max_length=50, blank=True, null=True, verbose_name='homeless dove', choices=CARTELLA_SOCIALE_homelesstip)
    telef = models.CharField(max_length=16, null=True, verbose_name='telefono')
    richiesta = models.CharField(max_length=50, blank=True, null=True, choices=CARTELLA_SOCIALE_richiesta)
    orinetamento = models.CharField(max_length=50, blank=True, null=True, verbose_name='orientato a', choices=CARTELLA_SOCIALE_orinetamento)
    tessmensa = models.BooleanField(default=False, verbose_name='tessera mensa')
    scadtessmen = models.DateField(blank=True, null=True, verbose_name='scadenza')
    ssn = models.BooleanField(default=False, verbose_name='servizio san.naz.')
    ssntess = models.CharField(max_length=50, blank=True, null=True, verbose_name='tess.n.')
    ssnscad = models.DateField(blank=True, null=True, verbose_name='scadenza')
    pass_field = models.BooleanField(db_column='pass', default=False, verbose_name='passaporto')  # Field renamed because it was a Python reserved word.
    esenz = models.BooleanField(default=False, verbose_name='essenzioni')
    esenznum = models.CharField(max_length=50, blank=True, null=True, verbose_name='specifiche')
    stp = models.BooleanField(default=False)
    stpnum = models.CharField(max_length=50, blank=True, null=True, verbose_name='numero')
    stpscad = models.DateField(blank=True, null=True, verbose_name='scadenza')
    medicobase = models.BooleanField(default=False, verbose_name='medico di base')
    medicobasenom = models.CharField(max_length=50, blank=True, null=True, verbose_name='nominativo')
    medicobasetel = models.CharField(max_length=50, blank=True, null=True, verbose_name='telefono')
    salutement = models.BooleanField(default=False, verbose_name='salute mentale')
    salutementop = models.CharField(max_length=50, blank=True, null=True, verbose_name='nominativo')
    salutementtel = models.CharField(max_length=50, blank=True, null=True, verbose_name='telefono')
    sert = models.BooleanField(default=False)
    sertop = models.CharField(max_length=50, blank=True, null=True, verbose_name='nominativo')
    serttel = models.CharField(max_length=50, blank=True, null=True, verbose_name='telefono')
    servsoc = models.IntegerField(blank=True, null=True)
    servsocop = models.CharField(max_length=50, blank=True, null=True)
    servsoctel = models.CharField(max_length=50, blank=True, null=True)
    docclinica = models.IntegerField(blank=True, null=True)
    freq = models.CharField(max_length=255, blank=True, null=True)
    nlett = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    posta = models.CharField(max_length=255, blank=True, null=True)
    ind = models.CharField(max_length=50, blank=True, null=True, verbose_name='persona', choices=CARTELLA_SOCIALE_ind)
    note = models.TextField(blank=True, null=True)
    emerg = models.IntegerField(blank=True, null=True)
    liv01_accesso = models.CharField(db_column='Liv01_accesso', max_length=50, blank=True, null=True, verbose_name='accesso', choices=ACCOGLIENZA_RESIDENZIALE_liv01_accesso)  # Field name made lowercase.
    liv01_servizio = models.CharField(db_column='Liv01_servizio', max_length=50, blank=True, null=True, verbose_name='servizio', choices=ACCOGLIENZA_RESIDENZIALE_liv01_servizio)  # Field name made lowercase.
    liv01_operatore = models.CharField(db_column='Liv01_operatore', max_length=90, blank=True, null=True, verbose_name='operatore: nome, tel, mail')  # Field name made lowercase.
    liv01_servutilizzati = models.TextField(db_column='Liv01_servutilizzati', blank=True, null=True, verbose_name='servizi utilizzati: breve descrizione')  # Field name made lowercase.
    liv01_motivo = models.CharField(db_column='Liv01_motivo', max_length=50, blank=True, null=True, verbose_name='presa in carico per', choices=ACCOGLIENZA_RESIDENZIALE_liv01_motivo)  # Field name made lowercase.
    liv01_status = models.BooleanField(db_column='Liv01_status', default=False, verbose_name='coniugato')  # Field name made lowercase.
    liv01_coniuge = models.CharField(db_column='Liv01_coniuge', max_length=50, blank=True, null=True, verbose_name='coniuge')  # Field name made lowercase.
    liv01_figli = models.CharField(db_column='Liv01_figli', max_length=50, blank=True, null=True, verbose_name='figli')  # Field name made lowercase.
    liv01_altririf = models.CharField(db_column='Liv01_altririf', max_length=50, blank=True, null=True, verbose_name='altro')  # Field name made lowercase.
    liv01_famiglia = models.TextField(db_column='Liv01_famiglia', blank=True, null=True, verbose_name='breve descrizione, se fornisce sostegno, condizione ...')  # Field name made lowercase.
    liv01_abitaz = models.CharField(db_column='Liv01_abitaz', max_length=50, blank=True, null=True, verbose_name='abitazione', choices=UTENTI_liv01_abitaz)  # Field name made lowercase.
    liv01_senzadim = models.BooleanField(db_column='Liv01_senzadim', default=False, verbose_name='senza dimora')  # Field name made lowercase.
    liv01_notte = models.CharField(db_column='Liv01_notte', max_length=50, blank=True, null=True, verbose_name='dove passa la notte a modena')  # Field name made lowercase.
    liv01_condprof = models.CharField(db_column='Liv01_condprof', max_length=50, blank=True, null=True, verbose_name='cond.profess.')  # Field name made lowercase.
    liv01_reddito = models.BooleanField(db_column='Liv01_reddito', default=False, verbose_name='reddito')  # Field name made lowercase.
    liv01_reddliv = models.CharField(db_column='Liv01_reddliv', max_length=50, blank=True, null=True, verbose_name='livello di redito')  # Field name made lowercase.
    liv01_ultimolavoro = models.CharField(db_column='Liv01_ultimolavoro', max_length=50, blank=True, null=True, verbose_name='ultimo lavoro')  # Field name made lowercase.
    liv01_tipologia = models.CharField(db_column='Liv01_tipologia', max_length=50, blank=True, null=True, verbose_name='contratto', choices=UTENTI_liv01_tipologia)  # Field name made lowercase.
    liv01_azienda = models.CharField(db_column='Liv01_azienda', max_length=50, blank=True, null=True, verbose_name='azienda: rif. e tel')  # Field name made lowercase.
    liv01_formprof = models.BooleanField(db_column='Liv01_formprof', default=False, verbose_name='formaz prof')  # Field name made lowercase.
    liv01_formprofdescr = models.CharField(db_column='Liv01_formprofdescr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    livo01_italiano = models.CharField(db_column='Livo01_italiano', max_length=50, blank=True, null=True, verbose_name='italiano', choices=UTENTI_livo01_italiano)  # Field name made lowercase.
    liv01_tititaliano = models.CharField(db_column='Liv01_tititaliano', max_length=50, blank=True, null=True, verbose_name='titolo di studio italiano')  # Field name made lowercase.
    liv01_titstran = models.CharField(db_column='Liv01_titstran', max_length=50, blank=True, null=True, verbose_name='titolo di studio straniero')  # Field name made lowercase.
    liv01_pat = models.IntegerField(db_column='Liv01_pat', blank=True, null=True, verbose_name='patente')  # Field name made lowercase.
    liv01_ci = models.IntegerField(db_column='Liv01_ci', blank=True, null=True, verbose_name='scritto centro impiego')  # Field name made lowercase.
    liv01_suss = models.CharField(db_column='Liv01_suss', max_length=50, blank=True, null=True, verbose_name='sussidi/disoccupazione')  # Field name made lowercase.
    liv01_pens = models.CharField(db_column='Liv01_pens', max_length=50, blank=True, null=True, verbose_name='pensione')  # Field name made lowercase.
    liv03_req = models.BooleanField(db_column='Liv03_req', default=False, verbose_name='requisiti accesso sportello avvocato')  # Field name made lowercase.
    liv03_tipologia = models.CharField(db_column='Liv03_tipologia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    liv03_avvoc = models.CharField(db_column='Liv03_avvoc', max_length=255, blank=True, null=True, verbose_name='avvocato di riferimento, telefono, mail')  # Field name made lowercase.
    liv03_note = models.TextField(db_column='Liv03_note', blank=True, null=True, verbose_name='Problematica Risoluzione')  # Field name made lowercase.
    liv04_dormit = models.BooleanField(db_column='Liv04_dormit', default=False, verbose_name='dormitorio')  # Field name made lowercase.
    liv04_servizio = models.CharField(db_column='Liv04_servizio', max_length=255, blank=True, null=True, choices=ACCOGLIENZA_RESIDENZIALE_liv04_servizio, verbose_name='servizio di accoglienza')  # Field name made lowercase.
    liv04_tipologia = models.CharField(db_column='Liv04_tipologia', max_length=255, blank=True, null=True, choices=ACCOGLIENZA_RESIDENZIALE_liv04_tipologia, verbose_name='tipologia')  # Field name made lowercase.
    liv04_allprov = models.CharField(db_column='Liv04_allprov', max_length=255, blank=True, null=True, choices=ACCOGLIENZA_RESIDENZIALE_liv04_allprov, verbose_name='condizione alloggiativa di provenienza')  # Field name made lowercase.
    liv04_statusacc = models.CharField(db_column='Li04_statusacc', blank=True, null=True, max_length=50, choices=ACCOGLIENZA_RESIDENZIALE_liv04_statusacc, verbose_name='status accogl.')  # Field name made lowercase.
    liv04_amm = models.DateTimeField(db_column='Liv04_amm', blank=True, null=True, verbose_name='ammissione')  # Field name made lowercase.
    liv04_dimmprev = models.DateTimeField(db_column='Liv04_dimmprev', blank=True, null=True, verbose_name='dimissione')  # Field name made lowercase.
    liv04_dimm = models.DateTimeField(db_column='Liv04_dimm', blank=True, null=True)  # Field name made lowercase.
    liv04_acccoll = models.CharField(db_column='Liv04_acccoll', blank=True, null=True, max_length=255, choices=ACCOGLIENZA_RESIDENZIALE_liv04_acccoll, verbose_name='Accoglienza collegata a')  # Field name made lowercase.
    liv04_acccoll_dal = models.DateTimeField(db_column='Liv04_acccoll_dal', blank=True, null=True, verbose_name='accoglienza collegata al')  # Field name made lowercase.
    liv04_acccoll_al = models.DateTimeField(db_column='Liv04_acccoll_al', blank=True, null=True, verbose_name='accoglienza collegata al')  # Field name made lowercase.
    liv04_profilo = models.TextField(db_column='Liv04_profilo', blank=True, null=True, verbose_name='profillo: breve nota su aspetti positivi/negativi riscontrati durante la permanenza')  # Field name made lowercase.
    liv04_motdimm = models.CharField(db_column='Liv04_motdimm', max_length=255, blank=True, null=True, choices=ACCOGLIENZA_RESIDENZIALE_liv04_motdimm, verbose_name='Motivo dimissione')  # Field name made lowercase.
    liv04_conddimm = models.CharField(db_column='Liv04_conddimm', blank=True, null=True, max_length=255, choices=ACCOGLIENZA_RESIDENZIALE_liv04_conddimm, verbose_name='Alloggio dopo dimissione')  # Field name made lowercase.
    liv05_titolare = models.CharField(db_column='Liv05_titolare', max_length=255, blank=True, null=True, verbose_name='titolare del case: nominativo, tel, mail')  # Field name made lowercase.
    liv05_refapa = models.CharField(db_column='Liv05_refapa', max_length=255, blank=True, null=True, verbose_name='referente interno apa')  # Field name made lowercase.
    liv05_obiett = models.CharField(db_column='Liv05_obiett', max_length=255, blank=True, null=True, verbose_name='obiettivo: descr')  # Field name made lowercase.
    liv05_duratadal = models.DateField(db_column='Liv05_duratadal', blank=True, null=True, verbose_name='dal')  # Field name made lowercase.
    liv05_durataal = models.DateField(db_column='Liv05_durataal', blank=True, null=True, verbose_name='al')  # Field name made lowercase.
    liv05_descrcrit = models.TextField(db_column='Liv05_descrcrit', blank=True, null=True, verbose_name="CRITICITA'")  # Field name made lowercase.
    liv05_descrris = models.TextField(db_column='Liv05_descrris', blank=True, null=True, verbose_name='RISORSE')  # Field name made lowercase.
    liv05_servapa = models.TextField(db_column='Liv05_servapa', blank=True, null=True, verbose_name='SERVIZI RICHIESTI A PORTA APERTA')  # Field name made lowercase.
    liv05_servaltri = models.TextField(db_column='Liv05_servaltri', blank=True, null=True, verbose_name='RETE DEI SERVIZI COINVOLTI')  # Field name made lowercase.
    liv05_imppers = models.TextField(db_column='Liv05_imppers', blank=True, null=True, verbose_name='IMPEGNI DELLA PERSONA')  # Field name made lowercase.
    liv05_aggiorn = models.TextField(db_column='Liv05_aggiorn', blank=True, null=True, verbose_name='AGGIORNAMENTO E DIARIO: DATA, RILEVAZIONE, TIPO DI INTERVENTO, SOGETTI COINVOLTI')  # Field name made lowercase.
    liv05_oretit_refapa = models.CharField(max_length=30, db_column='Liv05_oretit/refapa', blank=True, null=True, verbose_name='Ore settimanali (titolare/referente apa)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    liv05_collagg = models.IntegerField(db_column='Liv05_collagg', blank=True, null=True, verbose_name='N. colloqui aggiornamento con utente')  # Field name made lowercase.
    liv05_incontriinv = models.IntegerField(db_column='Liv05_incontriinv', blank=True, null=True, verbose_name='N. incontri con operatori invianti')  # Field name made lowercase.
    liv05_volcoinv = models.IntegerField(db_column='Liv05_volcoinv', blank=True, null=True, verbose_name='N.volontarii coinvolti')  # Field name made lowercase.
    liv05_contrapa = models.DecimalField(db_column='Liv05_contrapa', max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='Tot. contributo economico apa')  # Field name made lowercase.
    liv05_conclprog = models.DateField(db_column='Liv05_conclprog', blank=True, null=True, verbose_name='conclusione del progetto personale')  # Field name made lowercase.
    liv05_famiglia = models.CharField(db_column='Liv05_famiglia', max_length=255, blank=True, null=True, verbose_name='famiglia', choices=UTENTI_liv05_famiglia)  # Field name made lowercase.
    liv05_lavoro = models.CharField(db_column='Liv05_lavoro', max_length=255, blank=True, null=True, verbose_name='lavoro', choices=UTENTI_liv05_lavoro)  # Field name made lowercase.
    liv05_salute = models.CharField(db_column='Liv05_salute', max_length=255, blank=True, null=True, verbose_name='salute', choices=UTENTI_liv05_salute)  # Field name made lowercase.
    liv05_diritti = models.CharField(db_column='Liv05_diritti', max_length=255, blank=True, null=True, verbose_name='diritti', choices=UTENTI_diritti)  # Field name made lowercase.
    liv05_alloggio = models.CharField(db_column='Liv05_alloggio', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'utenti'
        verbose_name = 'Persona'
        verbose_name_plural = 'Persone'

    def __unicode__(self):
        return "%s" % self.nom

    def __str__(self):
        return "%s %s" % (self.nom, self.cogn)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % self.foto.url)

    image_tag.short_description = 'foto'


class Avvocati(models.Model):
    id_avv = models.AutoField(db_column='ID_avv', primary_key=True)  # Field name made lowercase.
    # id_ut = models.IntegerField(db_column='ID_UT', blank=True, null=True)  # Field name made lowercase.
    id_ut = models.ForeignKey(Utenti, db_column='ID_UT', blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    id = models.ForeignKey('Giurisprud', blank=True, null=True)
    problema = models.TextField(blank=True, null=True, verbose_name='problematica legale presentata')
    soluzione = models.TextField(blank=True, null=True, verbose_name='soluzione adottata')

    class Meta:
        managed = True
        db_table = 'Avvocati'
        verbose_name_plural = 'AVVOCATI'
    # def __unicode__(self):
    #     return '%s %s %s' % (self.id_ut, self.cogn, self.nom)
    #
    # def __str__(self):
    #     return '%s %s %s' % (self.id_ut, self.cogn, self.nom)


class Uds(models.Model):
    id_uds = models.AutoField(db_column='ID_uds', primary_key=True)  # Field name made lowercase.
    # id_ut = models.IntegerField(db_column='ID_ut', blank=True, null=True)  # Field name made lowercase.
    id_ut = models.ForeignKey(Utenti, db_column='ID_ut', blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    ora = models.DateTimeField(blank=True, null=True)
    luogo = models.CharField(max_length=255, blank=True, null=True)
    condizioni = models.CharField(max_length=255, blank=True, null=True)
    servizio = models.CharField(max_length=255, blank=True, null=True)
    intervento = models.CharField(max_length=255, blank=True, null=True)
    segnalazione = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'uds'

    def __str__(self):
        return '%s %s' % (self.id_uds, self.id_ut)


class Citta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    continente = models.CharField(max_length=255, blank=True, null=True)
    stato = models.CharField(max_length=255, blank=True, null=True)
    citta = models.CharField(max_length=255, blank=True, null=True)
    prov = models.CharField(max_length=255, blank=True, null=True)
    cap = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '04_citta'

    def __str__(self):
        print('running str method')
        return "{}".format(self.citta)


class Ut(models.Model):
    id_serv = models.AutoField(db_column='ID_serv', primary_key=True)  # Field name made lowercase.
    # id_ut = models.IntegerField(db_column='ID_ut', blank=True, null=True)  # Field name made lowercase.
    id_ut = models.ForeignKey(Utenti, db_column='ID_ut', blank=True, null=True)
    oggi = models.DateField()
    mensa = models.BooleanField(default=False, verbose_name='rossa')
    no_tex = models.BooleanField(default=False, db_column='no tex')  # Field renamed to remove unsuitable characters.
    docce = models.BooleanField(default=False, verbose_name='blu')
    maga = models.BooleanField(default=False, verbose_name='maggazz')
    pranzo = models.BooleanField(default=False)
    indum = models.BooleanField(default=False, verbose_name='cop/sp')
    tex_scad = models.BooleanField(db_column='tex scad', default=False)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'ut'
        verbose_name = 'Servizi di base uttilizatiI'
        verbose_name_plural = 'Servizi di base uttilizati'

    def __str__(self):
        return '%s %s' % (self.id_ut.nom, self.id_ut.cogn)


class Visite(models.Model):
    id_visita = models.AutoField(db_column='ID_visita', primary_key=True)  # Field name made lowercase.
    # id_ut = models.IntegerField(db_column='ID_ut', blank=True, null=True)  # Field name made lowercase.
    id_ut = models.ForeignKey(Utenti, db_column='ID_ut', blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    patologie = models.ForeignKey('Malattie', blank=True, null=True)
    terapia = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visite'
        verbose_name_plural = 'AMBULATORIO - VISITE'

    def __str__(self):
        return '%s %s' %(self.id_visita, self.patologie)

class Magazz(models.Model):
    id_mag = models.AutoField(db_column='ID_mag', primary_key=True)  # Field name made lowercase.
    # id_ut = models.IntegerField(db_column='ID_ut', blank=True, null=True)  # Field name made lowercase.
    id_ut = models.ForeignKey(Utenti, db_column='ID_ut', blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    settore = models.CharField(max_length=50, blank=True, null=True, choices=CARTELLA_PORTENERIA_settore)
    data_fine = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'magazz'
        verbose_name = 'MAGAZZINO BORSE'
        verbose_name_plural = 'MAGAZZINO BORSE'


class Interventi(models.Model):
    id_interventi = models.AutoField(db_column='ID_interventi', primary_key=True)  # Field name made lowercase.
    # id_ut = models.IntegerField(db_column='ID_ut', blank=True, null=True)  # Field name made lowercase.
    id_ut = models.ForeignKey(Utenti, db_column='ID_ut')
    interventi = models.CharField(max_length=50, blank=True, null=True, choices=INTERVENTI_interventi)
    tempo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Interventi'
        verbose_name='Intervento'
        verbose_name_plural = 'interventi'


class ElencoIndirizzi(models.Model):
    idelenco_indirizzi = models.AutoField(db_column='IDElenco indirizzi', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prefisso = models.CharField(db_column='Prefisso', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Elenco indirizzi'


class ErroriDiIncollamento(models.Model):
    campo0 = models.TextField(db_column='Campo0', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Errori di incollamento'


class Livello01(models.Model):
    id_liv01 = models.AutoField(db_column='ID_LIV01', primary_key=True)  # Field name made lowercase.
    id_ut = models.IntegerField(db_column='ID_UT', blank=True, null=True)  # Field name made lowercase.
    accesso = models.CharField(max_length=50, blank=True, null=True)
    servizio = models.CharField(max_length=50, blank=True, null=True)
    operatore = models.CharField(max_length=50, blank=True, null=True)
    serviziutilizzati = models.CharField(max_length=50, blank=True, null=True)
    motivoprev = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Livello_01'


class Msyscompacterror(models.Model):
    errorcode = models.IntegerField(db_column='ErrorCode', blank=True, null=True)  # Field name made lowercase.
    errordescription = models.TextField(db_column='ErrorDescription', blank=True, null=True)  # Field name made lowercase.
    errorrecid = models.TextField(db_column='ErrorRecid', blank=True, null=True)  # Field name made lowercase.
    errortable = models.CharField(db_column='ErrorTable', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MSysCompactError'

from django.core.validators import validate_email

class Risorse(models.Model):
    tip_risorsa = models.CharField(max_length=50, blank=True, null=True, verbose_name='tipologia di risorsa', choices=RISORSE_tip)
    riferim = models.CharField(max_length=50, blank=True, null=True, verbose_name='riferimento: nominativo')
    riferim_ente = models.CharField(unique=True, max_length=50, blank=True, null=True, verbose_name='riferimento ente/organismo')
    telefono = models.CharField(max_length=255, blank=True, null=True)
    mail = models.EmailField(max_length=255, blank=True, null=True, validators=[validate_email,])
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Risorse'
        verbose_name = 'Risorse'
        verbose_name_plural = 'Risorse'


class SwitchboardItems(models.Model):
    switchboardid = models.IntegerField(db_column='SwitchboardID')  # Field name made lowercase.
    itemnumber = models.IntegerField(db_column='ItemNumber')  # Field name made lowercase.
    itemtext = models.CharField(db_column='ItemText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    command = models.IntegerField(db_column='Command', blank=True, null=True)  # Field name made lowercase.
    argument = models.CharField(db_column='Argument', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Switchboard Items'
        unique_together = (('switchboardid', 'itemnumber'),)


class Cucina(models.Model):
    id_cuc = models.AutoField(primary_key=True)
    oggi = models.DateField()
    pasti = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cucina'


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_migrations'

GENERE = (
    ('M', 'M'),
    ('F', 'F'),
)
class Donazioni(models.Model):
    id_ut = models.AutoField(db_column='ID ut', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anno = models.CharField(max_length=50, blank=True, null=True)
    oggi = models.DateField()
    op = models.CharField(max_length=50)
    cogn = models.CharField(max_length=50, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True, verbose_name='nome')
    nasc = models.DateField(blank=True, null=True, verbose_name='Data di Nascita', validators=[validate_nascita])
    eta = models.CharField(max_length=50, blank=True, null=True, verbose_name='età')
    paese = models.IntegerField(blank=True, null=True)
    sesso = models.CharField(max_length=50, blank=True, null=True, choices=GENERE)
    via = models.CharField(max_length=50, blank=True, null=True)
    citta = models.CharField(max_length=50, blank=True, null=True, verbose_name='Città')
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    ncolli = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'donazioni'
        verbose_name = 'Donazione'
        verbose_name_plural = 'Donazioni'

class Giurisprud(models.Model):
    cod = models.CharField(unique=True, max_length=5, blank=True, null=True)
    gen = models.CharField(max_length=50, blank=True, null=True)
    sottoge = models.CharField(unique=True, max_length=90, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'giurisprud'

    def __str__(self):
        return '%s %s' %(self.cod, self.gen)

class Malattie(models.Model):
    cod = models.CharField(unique=True, max_length=4, blank=True, null=True)
    gen = models.CharField(max_length=50, blank=True, null=True)
    sottoge = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'malattie'

    def __str__(self):
        ret = '%s  %s' %(self.cod, self.gen)
        return ret
