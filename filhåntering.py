import os  # Importerer os-modulen for å kunne jobbe med operativsystemavhengige funksjoner, som å sjekke filens eksistens

# Åpne og lukke filer
def lage_ny_fil():
    print("Lager en ny fil med initialt innhold.")
    # Åpner 'file.txt' i skrivemodus ('w'). Denne modusen vil opprette filen hvis den ikke eksisterer, og slette innholdet hvis den gjør
    with open('file.txt', 'w') as file:
        file.write("Dette er en lagret fil")  # Skriver initial tekst til filen

# Skrive til filer
def skrive_til_fil():
    print("Legger til en ny linje i filen.")
    # Åpner 'file.txt' i tilføyingsmodus ('a'), som legger til ny tekst på slutten av filen uten å slette eksisterende innhold
    with open('file.txt', 'a') as file:
        file.write("\nNy linje til teksten!")  # Legger til en ny linje i filen

# Lese fra filer
def les_hele_fil():
    print("\nLeser hele innholdet av filen:")
    # Åpner 'file.txt' i lesemodus ('r') for å lese hele innholdet som en enkel streng
    with open('file.txt', 'r') as file:
        content = file.read()  # Leser hele innholdet av filen
        print(content)  # Skriver ut innholdet til konsollen

def les_linje_for_linje():
    print("\nLeser filen linje for linje:")
    # Åpner 'file.txt' i lesemodus ('r') for å lese filen linje for linje
    with open('file.txt', 'r') as file:
        for line in file:
            print(line.strip())  # .strip() fjerner overflødige mellomrom og linjeendinger fra hver linje og skriver ut resultatet

# Filhåndteringstips
def finn_og_lese_fil():
    print("\nSjekker om filen eksisterer og leser den hvis den gjør:")
    # Bruker os.path.exists for å sjekke om 'file.txt' eksisterer i gjeldende katalog
    if os.path.exists('file.txt'):
        # Åpner filen i lesemodus og skriver ut innholdet hvis den eksisterer
        with open('file.txt', 'r') as file:
            print(file.read())
    else:
        # Informerer brukeren om at filen ikke eksisterer
        print("Filen eksisterer ikke!")

def main():
    print("\n--- Starter filhåndteringsdemonstrasjon ---\n")
    lage_ny_fil()           # Kaller funksjonen for å lage en ny fil
    skrive_til_fil()        # Kaller funksjonen for å legge til en linje i filen
    les_hele_fil()          # Kaller funksjonen for å skrive ut hele filens innhold
    les_linje_for_linje()   # Kaller funksjonen for å skrive ut hver linje individuelt
    finn_og_lese_fil()      # Kaller funksjonen som sjekker filens eksistens og leser den
    print("\n--- Fullførte filoperasjoner ---")

# Sikrer at main() utføres bare når skriptet kjøres direkte
if __name__ == "__main__":
    main()