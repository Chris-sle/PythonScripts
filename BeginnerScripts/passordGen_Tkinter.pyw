import random
import string
import tkinter as tk
from tkinter import simpledialog, messagebox

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

def create_password():
    website = simpledialog.askstring("Input", "Hvilken nettside er passordet til?")
    username = simpledialog.askstring("Input", "Hva er brukernavnet ditt?")
    
    try:
        length = int(simpledialog.askstring("Input", "Hvor langt skal passordet være?"))
        use_lowercase = simpledialog.askstring("Input", "Vil du ha små bokstaver? (ja/nei)").lower() == 'ja'
        use_uppercase = simpledialog.askstring("Input", "Vil du ha store bokstaver? (ja/nei)").lower() == 'ja'
        use_numbers = simpledialog.askstring("Input", "Vil du ha tall? (ja/nei)").lower() == 'ja'
        use_specials = simpledialog.askstring("Input", "Vil du ha spesialtegn? (ja/nei)").lower() == 'ja'

        if not any([use_lowercase, use_uppercase, use_numbers, use_specials]):
            messagebox.showerror("Error", "Du må velge minst én type tegn!")
            return

        password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_specials)
        
        # Skriv til fil med append ('a' mode)
        with open('password.txt', 'a') as file:
            file.write(f"{website} - {username} - {password}\n")
        
        messagebox.showinfo("Info", "Passordet er generert og lagret i 'password.txt'.")
    except ValueError:
        messagebox.showerror("Error", "Ugyldig lengde! Vennligst skriv et tall.")
    finally:
        root.quit()  # Avslutt GUI etter at oppgaven er fullført

# Lag GUI vindu
root = tk.Tk()
root.withdraw()  # Skjul hovedvinduet
create_password()
root.mainloop()