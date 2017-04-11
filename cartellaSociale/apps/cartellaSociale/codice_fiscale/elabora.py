import string
import os
# vedi http://it.wikipedia.org/wiki/Codice_fiscale
# per una spiegazione piu' dettagliata dell'algoritmo

class variabili:
    def __init__(self):
        # type: () -> object
        self.vocali = []
        self.consonanti = []
        self.tabella_mese = ['a', 'b', 'c', 'd', 'e', 'h', 'l', 'm', 'p', 'r', 's', 't']
        self.tabella_pari = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
                             '9': '9', 'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7',
                             'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15',
                             'q': '16', 'r': '17', 's': '18', 't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23',
                             'y': '24', 'z': '25'}
        self.tabella_dispari = {'0': '1', '1': '0', '2': '5', '3': '7', '4': '9', '5': '13', '6': '15', '7': '17',
                                '8': '19', '9': '21', 'a': '1', 'b': '0', 'c': '5', 'd': '7', 'e': '9', 'f': '13',
                                'g': '15', 'h': '17', 'i': '19', 'j': '21', 'k': '2', 'l': '4', 'm': '18', 'n': '20',
                                'o': '11', 'p': '3', 'q': '6', 'r': '8', 's': '12', 't': '14', 'u': '16', 'v': '10',
                                'w': '22', 'x': '25', 'y': '24', 'z': '23'}
        self.tabella_resto = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
                              11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
                              21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
        self.comuni = []
        self.nome = ''
        self.cognome = ''
        self.data = ''
        self.giorno = ''
        self.mese = ''
        self.anno = ''
        self.sesso = ''
        self.codice_catastale = ''
        self.codice_incompleto = ''
        self.cifre_pari = []
        self.cifre_dispari = []
        self.lettera_di_controllo = ''
        self.codice_fiscale = ''


def smista(var):
    # divido le vocali dalle cosonanti
    x = 0
    while x < len(var):
        if var[x] == 'a' or var[x] == 'e' or var[x] == 'i' or var[x] == 'o' or var[x] == 'u':
            v.vocali.append(var[x])
        else:
            v.consonanti.append(var[x])
        x += 1


def cognome(var):
    # Vengono prese le consonanti del cognome (o dei cognomi, se ne ha piu' di uno)
    # nel loro ordine: solo se sono insufficienti, si prelevano anche le vocali,
    # sempre nel loro ordine: comunque, le vocali vengono riportate dopo le consonanti.
    # Nel caso in cui cognome abbia meno di tre lettere, la parte di codice viene
    # completata aggiungendo la lettera X (es.: Fo -> FOX).

    smista(var)
    if len(v.consonanti) >= 3:
        v.cognome = v.consonanti[0] + v.consonanti[1] + v.consonanti[2]
    elif len(v.consonanti) == 2 and len(v.vocali) >= 1:
        v.cognome = v.consonanti[0] + v.consonanti[1] + v.vocali[0]
    elif len(v.consonanti) == 1 and len(v.vocali) >= 2:
        v.cognome = v.consonanti[0] + v.vocali[0] + v.vocali[1]
    else:
        v.cognome = v.consonanti[0] + v.vocali[0] + 'x'
    del v.consonanti[:]
    del v.vocali[:]


def nome(var):
    # Vengono prese le consonanti del nome (o dei nomi, se ve ne e' piu' di uno)
    # in questo modo: se il nome contiene quattro o piu' consonanti, si scelgono
    # la prima, la terza e la quarta, altrimenti le prime tre in ordine.
    # Solo se il nome non ha consonanti a sufficienza, si prendono anche le vocali:
    # comunque, le vocali vengono riportate dopo le consonanti. Nel caso in cui
    # il nome abbia meno di tre lettere, la parte di codice viene completata
    # aggiungendo la lettera X.

    smista(var)
    if len(v.consonanti) > 3:
        v.nome = v.consonanti[0] + v.consonanti[2] + v.consonanti[3]
    elif len(v.consonanti) >= 3:
        v.nome = v.consonanti[0] + v.consonanti[1] + v.consonanti[2]
    elif len(v.consonanti) == 2 and len(v.vocali) >= 1:
        v.nome = v.consonanti[0] + v.consonanti[1] + v.vocali[0]
    elif len(v.consonanti) == 1 and len(v.vocali) >= 2:
        v.nome = v.consonanti[0] + v.vocali[0] + v.vocali[1]
    else:
        v.nome = v.consonanti[0] + v.vocali[0] + 'x'
    del v.consonanti[:]
    del v.vocali[:]


def data(data):
    data = data.split('/')
    v.data = data

    # Anno di nascita (2 cifre): si prendono le ultime
    # due cifre dell'anno di nascita
    v.anno = v.data[2][-2:]

    # Mese di nascita (1 lettera): ad ogni mese dell'anno
    # viene associata una lettera in base a tabella_mese
    v.mese = v.tabella_mese[int(v.data[1]) - 1]

    # Giorno di nascita e sesso (2 cifre): si prendono le due cifre
    # del giorno di nascita (se e' compreso tra 1 e 9 si pone uno zero
    # come prima cifra); per i soggetti di sesso femminile a tale cifra
    # va sommato il numero 40
    print('++++++++++++++++++++++++++++++++', v.giorno)
    if v.sesso == 'm':
        if (int(v.data[0]) > 9) or (len(v.data[0]) == 2):
            v.giorno = str(v.data[0])
        else:
            v.giorno = "0" + v.data[0]
    else:
        v.giorno = str(40 + int(data[0]))
    print('++++++++++++++++++++++++++++++++', v.giorno)


def comune(comune):
    file_path = os.path.join(os.path.dirname(__file__), 'codici_catastali_updated.txt')
    file = open(file_path, 'rU')

    # creo lista contenente i comuni con relativo codice catastale
    for line in file:
        v.comuni.append(line.split(','))
    for item in v.comuni:
        if comune == item[0].lower():
            print('*********************  comune found in item [0]')
            v.codice_catastale = item[1]
    del v.comuni[:]


def lettera_di_controllo():
    v.codice_incompleto = v.cognome + v.nome + v.anno + v.mese + v.giorno + v.codice_catastale
    # print (v.cognome, v.nome, v.anno, v.mese, v.giorno, v.codice_catastale)
    pari = v.codice_incompleto[1::2]
    dispari = v.codice_incompleto[::2]

    for item in pari:
        v.cifre_pari.append(int(v.tabella_pari[item]))

    for item in dispari:
        v.cifre_dispari.append(int(v.tabella_dispari[item]))

    # sommo tutte le cifre in posizione pari
    somma_pari = 0
    for item in v.cifre_pari:
        somma_pari = somma_pari + item
    # sommo tutte le cifre in posizione dispari
    somma_dispari = 0
    for item in v.cifre_dispari:
        somma_dispari = somma_dispari + item
    # sommo la somma dei pari e dei dispari
    somma = somma_pari + somma_dispari
    resto = somma % 26
    v.lettera_di_controllo = v.tabella_resto[resto]
    v.codice_fiscale = (v.codice_incompleto + v.lettera_di_controllo).upper()
    del v.cifre_pari[:]
    del v.cifre_dispari[:]


v = variabili()
