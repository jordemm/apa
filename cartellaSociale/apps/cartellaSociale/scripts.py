from cartellaSociale.apps.cartellaSociale.models import Utenti, Uds, Citta, Malattie

ut_1 = Utenti.objects.get_or_create(cf='utenteUnoCf', nom='UtenteUnoNome', cogn='UtenteUnoCognome', anno='2013-05-12', luogo='Modena', nasc='1913-05-12', status='Single')[0]
ut_2 = Utenti.objects.get_or_create(cf='utenteDueCf', nom='UtenteDueNome', cogn='UtenteDueCognome', anno='2014-02-22', luogo='mantova', nasc='2013-05-12', status='Married')[0]
ut_3 = Utenti.objects.get_or_create(cf='utenteTreCf', nom='UtenteTreNome', cogn='UtenteTreCognome', anno='2013-03-33', luogo='Bologna', nasc='1713-05-12', status='Single')[0]
ut_4 = Utenti.objects.get_or_create(cf='utenteQuattroCf', nom='UtenteQuattroNome', cogn='UtenteQuattroCognome', anno='2014-04-14', luogo='Roma', nasc='2013-05-12', status='Married')[0]
ut_5 = Utenti.objects.get_or_create(cf='utenteCinqueCf', nom='UtenteCinqueNome', cogn='UtenteCinqueCognome', anno='2015-05-15', luogo='Vincenza', nasc='2010-05-12', status='Single')[0]
ut_6 = Utenti.objects.get_or_create(cf='utentePippoCf', nom='pippo', cogn='UtenteUnoCognome', anno='2014-02-22', luogo='Modena', nasc='1713-05-12', status='Single')[0]
ut_7 = Utenti.objects.get_or_create(cf='utentePippoCf', nom='pippo', cogn='UtentePippoCognome', anno='2013-03-33', luogo='Bologna', nasc='2013-05-12', status='Married')[0]

ud_1 = Uds.objects.get_or_create(id_ut=ut_3, luogo='Parma', data='2010-06-21')
ud_2 = Uds.objects.get_or_create(id_ut=ut_3, luogo='Modena', data='2008-06-16')
ud_3 = Uds.objects.get_or_create(id_ut=ut_5, luogo='Parma', data='2010-06-05')
ud_4 = Uds.objects.get_or_create(id_ut=ut_5, luogo='Bologna', data='2011-07-11')
ud_5 = Uds.objects.get_or_create(id_ut=ut_1, luogo='Milano', data='2011-07-11')


citta_1 = Citta.objects.get_or_create(continente='Europe', stato='Italia', citta='Bazzano', prov='Bologna', cap='40056')
citta_2 = Citta.objects.get_or_create(continente='Europe', stato='Germania', citta='Munich', prov='Munich', cap='40056')
citta_3 = Citta.objects.get_or_create(continente='Europe', stato='Spagna', citta='paris', prov='paris', cap='40056')

mal1 = Malattie.objects.get_or_create(cod='12G4', gen='gen 1', sottoge='sottopge 1')
mal2 = Malattie.objects.get_or_create(cod='8GT4', gen='gen 2', sottoge='sottopge 2')