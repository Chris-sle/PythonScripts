# Bruk import for å hente moduler og pakker.
import math

# Dette er en kommentar. Kommentarer starter med # i Python og blir ignorert av programmet.

# Definer en funksjon som heter say_hei
def say_hei():
    # Funksjonen print() brukes til å skrive ut tekst til terminalen
    print("Hei, verden!")  # Dette skriver "Hei, verden!" til skjermen.

def print_liste():
    liste = [1, 2, 3]  # liste er liste.
    for number in liste:  # Enkel for-løkke.
        print(number)

def print_dictionary():
    dictionary = {"navn": "Chris", "alder": 35} # Likt et Objekt i javaskript.
    print(dictionary)

def print_liste_with_dictionaries():
    liste_m_dictionary = [{"navn": "Protos", "alder": 4}, {"navn": "Akuma", "alder": 1}]
    for person in liste_m_dictionary:
        print(person)

import math

# Matte funksjoner
def lets_do_math():
    # Beregn kvadratroten av 16 og skriv ut resultatet
    kvadratrot = math.sqrt(16)
    print(f"Kvadratroten av 16 er: {kvadratrot}")

    # Skriv ut verdien av pi fra math-modulen
    print(f"Verdien av pi er: {math.pi}")

    # Beregn 2 hevet til 3 og skriv ut resultatet
    to_til_tre = math.pow(2, 3)
    print(f"2 hevet til 3 er: {to_til_tre}")

# Bruk brukerinndata
def greet_user():
    # Be brukeren om å skrive inn navnet sitt
    navn = input("Hva er navnet ditt? ")
    # Skriv ut en hilsen med navnet brukeren oppgav
    print(f"Heisan, {navn}!")

# Lister og Håndtering av Brukerens Inndata
def sum_numbers_from_user():
    # Initialiser en tom liste for å lagre tallene brukeren skriver inn
    tall_liste = []
    while True:
        # Be brukeren om å skrive inn et tall eller 'slutt' for å stoppe
        tall_str = input("Tast inn et tall (eller 'slutt' for å stoppe): ")
        if tall_str.lower() == 'slutt':  # Sjekk om brukeren skrev 'slutt'
            break  # Avbryt løkken hvis brukeren skrev 'slutt'
        try:
            # Konverter brukerens input til flyttall og legg til listen
            tall = float(tall_str)
            tall_liste.append(tall)
        except ValueError:
            # Håndter tilfeller der input ikke kan konverteres til et tall
            print("Ugyldig input! Vennligst tast inn et tall.")
    # Skriv ut summen av alle tallene i listen
    print(f"Summen av tallene er: {sum(tall_liste)}")

# Bruke argumenter
a = 5
b = 3

def use_args(a, b):
    # Beregn summen av a og b og skriv ut resultatet
    result = a + b
    print(result)

# Callback funksjoner:
def callback_function():
    # Returner tallet 2
    return 2

def use_callback_function(callback):
    # Kall på callback-funksjonen og legg 2 til resultatet
    return 2 + callback()

def print_callback():
    # Skriv ut resultatet av callback_function, som returnerer 2
    print(callback_function())  # Utskrift 2
    # Skriv ut resultatet av use_callback_function med callback_function som argument, som gir 4
    print(use_callback_function(callback_function))  # Utskrift 4

def callback_function_double():
    # Returner tallet 4
    return 4

def use_callbacks(callback1, callback2):
    # Kall på begge callback-funksjonene og returner summen av resultatene
    return callback1() + callback2()

def print_multiple_callbacks():
    # Skriv ut resultatet av use_callbacks med to callback-funksjoner, som gir 6
    print(use_callbacks(callback_function, callback_function_double))  # Utskrift 6

# Feilhåndtering
def safe_square_root():
    try:
        # Be brukeren om å skrive inn et tall for å finne kvadratroten
        tall = float(input("Tast inn et tall for å finne kvadratroten: "))
        # Skriv ut kvadratroten av tallet
        print(f"Kvadratroten av {tall} er: {math.sqrt(tall)}")
    except ValueError:
        # Håndter tilfeller der input ikke kan konverteres til et tall
        print("Vennligst tast inn et gyldig tall.")
    except Exception as e:
        # Generell feilhåndtering for andre potensielle feil
        print(f"Noe gikk galt: {e}")


# Styling og Struktur
def main():
    say_hei()
    print_liste()
    print_dictionary()
    print_liste_with_dictionaries()
    lets_do_math()
    use_args(a, b)
    print_callback()
    print_multiple_callbacks()
    greet_user()
    sum_numbers_from_user()
    safe_square_root()



if __name__ == "__main__":
    main()

# Ytterligere Muligheter og Utforskning:
# Moduler og Pakker: Utforsk hvordan du kan organisere koden din i flere moduler og pakker for bedre struktur, spesielt når skript blir større.
# Objektorientert Programmering (OOP): Implementering av klasser for bedre å forstå OOP-konsepter.
# Filhåndtering: Lær hvordan du kan lese fra og skrive til filer for å utvide din forståelse av IO-operasjoner.
# Asynkrone Operasjoner: Bruk modulen 'asyncio' for å håndtere tidkrevende operasjoner uten å blokkere utførelsen av andre operasjoner.