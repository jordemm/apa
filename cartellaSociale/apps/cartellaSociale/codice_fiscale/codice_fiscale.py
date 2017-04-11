from . import elabora


def calcola(cognome, nome, sesso, data, comune):
    print('--------------------------', nome, cognome, data, sesso, comune)
    # passo le variabili alle funzioni
    elabora.cognome(cognome)
    elabora.nome(nome)
    if sesso == 'm':
        elabora.v.sesso = 'm'
    else:
        elabora.v.sesso = 'f'
    elabora.data(data)
    elabora.comune(comune)
    elabora.lettera_di_controllo()
    print("Il tuo codice fiscale e':\n%s\n" % elabora.v.codice_fiscale)
    return elabora.v.codice_fiscale



if __name__ == '__main__':
    print("\tCalcola il tuo codice fiscale\n")

    # nome = 'emmanuel', cognome = 'osarenkhoe', sesso = 'm', data = '24/05/1988', comune = 'nigeria'
    codice_fiscale = calcola()
