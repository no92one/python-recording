contact_book = {}

while True:
    print('''\n--- Kontaktbok Meny ---
1. Lägg till ny kontakt
2. Uppdatera kontakt
3. Ta bort kontakt
4. Visa alla kontakter
5. Avsluta''')
    choice = input("Välj ett alternativ (1-5): ")

    if choice == '1':
        name = input("Ange namn: ")
        phone = input("Ange telefonnummer: ")
        email = input("Ange e-postadress: ")
        contact_book[name] = {"phone": phone, "email": email}
        print(f"Kontakt för {name} har lagts till.")
    
    elif choice == '2':
        name = input("Ange namnet på kontakten som ska uppdateras: ")
        if name in contact_book:
            phone = input("Ange nytt telefonnummer: ")
            email = input("Ange ny e-postadress: ")
            contact_book[name] = {"phone": phone, "email": email}
            print(f"Kontakt för {name} har uppdaterats.")
        else:
            print(f"Kontakt med namnet {name} hittades inte.")
    
    elif choice == '3':
        name = input("Ange namnet på kontakten som ska tas bort: ")
        if name in contact_book:
            del contact_book[name]
            print(f"Kontakt för {name} har tagits bort.")
        else:
            print(f"Kontakt med namnet {name} hittades inte.")
    
    elif choice == '4':
        if contact_book:
            print("\n--- Alla Kontakter ---")
            for name, info in contact_book.items():
                print(f"Namn: {name}")
                print(f"  Telefon: {info['phone']}")
                print(f"  E-post: {info['email']}")
        else:
            print("Kontaktboken är tom.")
    
    elif choice == '5':
        print("Avslutar programmet...")
        break
    
    else:
        print("Ogiltigt val, försök igen.")
