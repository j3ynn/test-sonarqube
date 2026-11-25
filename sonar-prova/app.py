# piccolo programma di prova per vedere cosa trova Sonar
# ATTENZIONE: contiene errori messi apposta

import os  # importato ma mai usato -> Sonar lo segnala


# password scritta direttamente nel codice -> problema di sicurezza
DB_PASSWORD = "admin123"


def somma(a, b):
    # funzione corretta, Sonar non dovrebbe dire niente
    return a + b


def dividi(a, b):
    # se b vale 0 il programma va in errore -> Sonar lo segnala come possibile bug
    risultato = a / b
    return risultato


def controlla_valore(x):
    # confronto con None scritto male (si usa "is None") -> code smell
    if x == None:
        return "vuoto"
    # variabile creata e mai usata -> code smell
    inutile = 42
    return "pieno"


def leggi_file(nome):
    try:
        with open(nome) as f:
            return f.read()
    except:
        # "except" senza tipo cattura TUTTI gli errori, anche quelli gravi -> code smell
        pass


if __name__ == "__main__":
    print(somma(2, 3))
    print(controlla_valore(None))