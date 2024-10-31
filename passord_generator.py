import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_specials):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("Du må velge minst én type tegn!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        website = input("Hvilken nettside er passordet til? ")
        username = input("Hva er brukernavnet ditt? ")
        length = int(input("Hvor langt skal passordet være? "))
        use_lowercase = input("Vil du ha små bokstaver? (ja/nei) ").lower() == 'ja'
        use_uppercase = input("Vil du ha store bokstaver? (ja/nei) ").lower() == 'ja'
        use_numbers = input("Vil du ha tall? (ja/nei) ").lower() == 'ja'
        use_specials = input("Vil du ha spesialtegn? (ja/nei) ").lower() == 'ja'

        if not any([use_lowercase, use_uppercase, use_numbers, use_specials]):
            print("Du må velge minst én type tegn!")
            return

        password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_specials)
        
        # Skriv til fil med append ('a' mode) for å sikre ny linje hvis filen allerede eksisterer
        with open('password.txt', 'a') as file:
            file.write(f"{website} - {username} - {password}\n")
        
        print("Passordet er generert og lagret i 'password.txt'.")
    except ValueError as e:
        print(e)
        print("Ugyldig input! Sørg for å skrive riktige verdier.")

if __name__ == "__main__":
    main()