ACCOGLIENZA_RESIDENZIALE_liv01_accesso = (
    ('DIRETTO', 'DIRETTO'),
    ('SU INVIO', 'SU INVIO'),
    ('INVIO A', 'INVIO A')
)

ACCOGLIENZA_RESIDENZIALE_liv01_servizio = (
    ('CENTRO ASCOLTO', 'CENTRO ASCOLTO'),
    ('CENTRO STRANIERI', 'CENTRO STRANIERI'),
    ('SERVIZIO SOCIALE', 'SERVIZIO SOCIALE'),
    ('SERT', 'SERT'),
    ('PREFETTURA', 'PREFETTURA'),
)


ACCOGLIENZA_RESIDENZIALE_liv01_motivo = (
    ('TUTELA SANITARIA', 'TUTELA SANITARIA'),
    ('RICERCA LAVORO', 'RICERCA LAVORO'),
    ('RICERCA ALLOGGIO', 'RICERCA ALLOGGIO'),
    ('STUDIO FORMAZIONE', 'STUDIO FORMAZIONE'),
    ('DOMICILIO TEMPORANEO', 'DOMICILIO TEMPORANEO'),
    ('ASILO POL RIFUGIATO', 'ASILO POL RIFUGIATO'),
    ('MISURE GIUDIZIARIE', 'MISURE GIUDIZIARIE'),
    ('ATTESA RIMPATRIO', 'ATTESA RIMPATRIO'),
    ('EMERGENZA', 'EMERGENZA'),
    ('EMERGENZA FREDDO', 'EMERGENZA FREDDO'),
)

ACCOGLIENZA_RESIDENZIALE_liv04_servizio = (
    ('COMUNE DI MODENA CONVENZIONE SERVIZIO SOCIALE', 'COMUNE DI MODENA CONVENZIONE SERVIZIO SOCIALE'),
    ('COMUNE DI MODENA CONVENZIONE CENTRO STRANIERI', 'COMUNE DI MODENA CONVENZIONE CENTRO STRANIERI'),
    ('COMUNE DI MODENA EMERGENZA FREDDO', 'COMUNE DI MODENA EMERGENZA FREDDO'),
    ('CENTRO ASCOLTO DIOCESANO', 'CENTRO ASCOLTO DIOCESANO'),
    ('PREFETTURA', 'PREFETTURA'),
    ('AUSL SERT', 'AUSL SERT'),
    ('PORTA APERTA', 'PORTA APERTA'),
    ('ALTRO', 'ALTRO'),
)

ACCOGLIENZA_RESIDENZIALE_liv04_tipologia = (
    ('PROGETTO', 'PROGETTO'),
    ('EMERGENZA', 'EMERGENZA'),
)

ACCOGLIENZA_RESIDENZIALE_liv04_allprov = (
    ('SENZA TETTO', 'SENZA TETTO'),
    ('SFRATTO', 'SFRATTO'),
    ('AUTO', 'AUTO'),
    ('CONVIVENZA', 'CONVIVENZA'),
)

ACCOGLIENZA_RESIDENZIALE_liv04_statusacc = (
    ('PRESENTE', 'PRESENTE'),
    ('DIMESSO', 'DIMESSO'),
)

ACCOGLIENZA_RESIDENZIALE_liv04_acccoll = (
    ('PARROCCHIA S.AGOSTINO', 'PARROCCHIA S.AGOSTINO'),
    ('PARROCCHIA BVA', 'PARROCCHIA BVA'),
    ('PARROCCHIA REGINA PACIS', 'PARROCCHIA REGINA PACIS'),
    ('PARROCCHIA GESÙ REDENTORE', 'PARROCCHIA GESÙ REDENTORE'),
    ('PARROCCHIA BAGGIOVARA', 'PARROCCHIA BAGGIOVARA'),
    ('PARROCCHIA S.ANTONIO', 'PARROCCHIA S.ANTONIO'),
    ('PARROCCHIA S.FAUSTINO', 'PARROCCHIA S.FAUSTINO'),
    ('APPARTAMENTO VIA GRAMSCI', 'APPARTAMENTO VIA GRAMSCI'),
    ('APPARTAMENTO VIA FREGNI', 'APPARTAMENTO VIA FREGNI'),
)

ACCOGLIENZA_RESIDENZIALE_liv04_conddimm = (
    ('APPARTAMENTO', 'APPARTAMENTO'),
    ('AFFITTACAMERE', 'AFFITTACAMERE'),
    ('ALTRA STRUTTURA', 'ALTRA STRUTTURA'),
    ('SENZA CASA', 'SENZA CASA'),
)

ACCOGLIENZA_RESIDENZIALE_liv04_motdimm = (
    ('CONCLUSIONE PROGETTO', 'CONCLUSIONE PROGETTO'),
    ('ALLONTANAMENTO ARBITRARIO', 'ALLONTANAMENTO ARBITRARIO'),
    ('INSERIMENTO ALTRA STRUTTURA', 'INSERIMENTO ALTRA STRUTTURA'),
    ('DIMISSIONE PER INFRAZIONE REGOLE', 'DIMISSIONE PER INFRAZIONE REGOLE'),
)


CARTELLA_SOCIALE_cittadinanza = (
    ('ITALIANA', 'ITALIANA'),
    ('EXTRA UE', 'EXTRA UE'),
    ('UE', 'UE'),
)

CARTELLA_SOCIALE_genere = (
    ('M', 'M'),
    ('F', 'F'),
)

CARTELLA_SOCIALE_status = (
    ('CELIBE', 'CELIBE'),
    ('CONGIUGATO', 'CONGIUGATO'),
    ('SEPARATO', 'SEPARATO'),
    ('DIVORZIATO', 'DIVORZIATO'),
)

CARTELLA_SOCIALE_doc = (
    ('PERMESSO DI SOGGIORNO', 'PERMESSO DI SOGGIORNO'),
    ('CARTA DI IDENTITA', 'CARTA DI IDENTITA'),
    ('PASSAPORTO', 'PASSAPORTO'),
    ('PATENTE', 'PATENTE'),
    ('ALTRO', 'ALTRO'),
    ('NESSUN DOCUMENTO', 'NESSUN DOCUMENTO')
)

CARTELLA_SOCIALE_tipologia_pds = (
    ('LAVORO AUTONOMO','LAVORO AUTONOMO'),
    ('LAVORO SUBORDINATO', 'LAVORO SUBORDINATO'),
    ('ATTESA OCCUPAZIONE', 'ATTESA OCCUPAZIONE'),
    ('SALUTE', 'SALUTE'),
    ('RICONGIUNGIMENTO', 'RICONGIUNGIMENTO')
)

CARTELLA_SOCIALE_homelesstip = (
    ('AUTO', 'AUTO'),
    ('ROULOTTE', 'ROULOTTE'),
    ('CASA ABBANDONATA', 'CASA ABBANDONATA'),
    ('STRADA', 'STRADA'),
    ('STAZIONE', ''),
    ('AMICI', 'STAZIONE'),
    ('PARENTI', 'PARENTI'),
    ('GARAGE', 'GARAGE')
)

CARTELLA_SOCIALE_richiesta = (
    ('PASTO', 'PASTO'),
    ('POSTO LETTO', 'POSTO LETTO'),
    ('LAVARSI', 'LAVARSI'),
    ('INDUMENTI', 'INDUMENTI'),
    ('COPERTE', 'COPERTE'),
    ('AVVOCATO DI STRADA', 'AVVOCATO DI STRADA')
)

CARTELLA_SOCIALE_orinetamento = (
    ('CENTRO ASCOLTO PER MENSA', 'CENTRO ASCOLTO PER MENSA'),
    ('CENTRO ASCOLTO PER POSTO LETTO', 'CENTRO ASCOLTO PER POSTO LETTO'),
    ('CENTRO STRANIERI PER POSTO LETTO', 'CENTRO STRANIERI PER POSTO LETTO'),
    ('SERVIZIO SOCIALE PER POSTO LETTO', 'SERVIZIO SOCIALE PER POSTO LETTO')
)

CARTELLA_SOCIALE_ind = (
    ('DARE APPUNTAMENTO', 'DARE APPUNTAMENTO'),
    ('INVIO CENTRO ASCOLTO', 'INVIO CENTRO ASCOLTO'),
    ('IN CARICO', 'IN CARICO'),
    ('IN ATTESA', 'IN ATTESA'),
    ('ATTENZIONE', 'ATTENZIONE'),
    ('INDESIDERATA', 'INDESIDERATA'),
    ('DIFFIDATA', 'DIFFIDATA'),
    ('SOSPESA', 'SOSPESA'),
    ('RIAMMESSA', 'RIAMMESSA'),
    ('NON SPECIFICATO', 'NON SPECIFICATO')
)

CARTELLA_PORTENERIA_settore = (
    ('A01', 'A01'),
    ('A02', 'A02'),
    ('A03', 'A03'),
    ('A04', 'A04'),
    ('A05', 'A05'),
    ('A06', 'A06'),
    ('A07', 'A07'),
    ('A08', 'A08'),
    ('B01', 'B01'),
    ('B02', 'B02'),
    ('B03', 'B03'),
    ('B04', 'B04'),
    ('B05', 'B05'),
    ('B06', 'B06'),
    ('B07', 'B07'),
    ('B08', 'B08'),
    ('C01', 'C01'),
    ('C02', 'C02'),
    ('C03', 'C03'),
    ('C04', 'C04'),
    ('C05', 'C05'),
    ('C06', 'C06'),
    ('C07', 'C07'),
    ('C08', 'C08'),
    ('D01', 'D01'),
    ('D02', 'D02'),
    ('D03', 'D03'),
    ('D04', 'D04'),
    ('D05', 'D05'),
    ('D06', 'D06'),
    ('D07', 'D07'),
    ('D08', 'D08'),
    ('E01', 'E01'),
    ('E02', 'E02'),
    ('E03', 'E03'),
    ('E04', 'E04'),
    ('E05', 'E05'),
    ('E06', 'E06'),
    ('E07', 'E07'),
    ('E08', 'E08'),
)


INTERVENTI_interventi = (
    ('Coloquio utente', 'Coloquio utente'),
    ('Colloquio servizi', 'Colloquio servizi'),
    ('Riunione', 'Riunione'),
    ('Equipe apa', 'Equipe apa'),
    ('Contatto Telefonico', 'Contatto Telefonico'),
    ('Relazione', 'Relazione'),
    ('Aggiornamento', 'Aggiornamento'),
)

UTENTI_liv05_famiglia =(
    ('Vive solo', 'Vive solo'),
    ('Vive nella propia famiglia', 'Vive nella propia famiglia'),
    ('Convive nuova famiglia', 'Convive nuova famiglia'),
    ('Convive con amici', 'Convive con amici')
)

UTENTI_liv05_lavoro = (
    ('Disoccupato', 'Disoccupato'),
    ('occupato', 'Occupato'),
    ('Pensionato', 'Pensionato')
)

UTENTI_liv05_salute = (
    ('Guarito', 'Guarito'),
    ('Malato', 'Malato'),
)

UTENTI_diritti =(
    ('Residente', 'Residente'),
    ('Senza dimora', 'Senza dimora'),
    ('Regolare', 'Regolare'),
    ('Irregolare', 'Irregolare')
)

RISORSE_tip = (
    ('Alloggio temporaneo', 'Alloggio temporaneo'),
    ('Appartamento', 'Appartamento'),
    ('Formazione professionale', 'Formazione professionale'),
    ('Corso italiano', 'Corso italiano'),
    ('Lavoro assistenza anziani', 'Lavoro assitenza anziani'),
    ('Lavoro pulizie', 'Lavoro pulizie'),
    ('Lavoro edilizia', 'Lavoro edilizia')
)

UTENTI_liv01_abitaz = (
    ('Propietà', 'Propietà'),
    ('Usufrutto', 'Usufrutto'),
    ('Affitto', 'Affitto'),
    ('Subaffitto', 'Subaffitto'),
    ('Casa popolare', 'Casa popolare'),
    ('Coabitazione', 'Coabitazione')
)

UTENTI_liv01_condprof = (
    ('Occupato', 'Occupato'),
    ('Disoccupato', 'Disoccupato'),
    ('Mobilità', 'Mobilità'),
    ('Cassa Integrazione', 'Cassa Integrazione')
)

UTENTI_liv01_tipologia = (
    ('TD tempo pieno', 'TD tempo pieno'),
    ('TD part time', 'TD part time'),
    ('TI tempo pieno', 'TI tempo pieno'),
    ('TI part time', 'TI part time'),
    ('Cocopro', 'Cocopro'),
    ('Voucher', 'Voucher'),
    ('Tirocinio', 'Tirocinio'),
    ('Stage', 'Stage')
)

UTENTI_livo01_italiano = (
    ('Scarsa', 'Scarsa'),
    ('Media', 'Media'),
    ('Buona', 'Buona')
)