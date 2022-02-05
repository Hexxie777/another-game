#Słownik - tutaj aktualizują się dane
book = {"AFK": "Away from keyboard"}


choice = None


while choice != "0":
    print("""
    Witaj w słowniku. Wybierz co chcesz zrobić: 
      0 - zakończ 
      1 - Znajdź słowo
      2 - Dodaj nowe słowo
      3 - Zmień znaczenie słowa
      4 - Pokaż słownik
      5 - Usuń słowo
    """)
    choice = input("Wybierasz: ")
    print()
    #Wyłączenie programu
    if choice == "0":
        print("Żegnaj")
    #Wyświetlanie definicji słowa ze słownika, jeżeli się w niej znajduje 
    elif choice == "1":
        term = input("Jaką definicję mam wyświetlić?: ")
        if term in book:
            definition = book[term]
            print("\n", term, "oznacza ", definition)
        else:
            print("Nie znam słowa", term)
    #Dodawanie terminu do słownika
    elif choice == "2":
        term = input("Jakie słowo mam dodać?: ")
        if term not in book:
            definition = input("Podaj definicję tego terminu: ")
            book[term] = definition
            print("Słowo", term, "został dodany")
        else:
            print("Ten termin już istnieje! Spróbuj zmienić jego definicję.")
    #Definiowanie istniejącego słowa
    elif choice == "3":
        term = input("Jakie słowo mam zdefiniować?: ")
        if term in book :
            definition = input("Jaka jest nowa definicja?: ")
            book[term] = definition
            print("\nSłowo",term, "zostało zdefiniowane")
        else:
            print("\nTe słowo nie istnieje! Spróbuj je dodać")
    #Wyświetlanie zawartości słownika
    elif choice == "4":
        print("W słowniku znajduje się: \n",book)
    #Usuwanie terminu
    elif choice == "5":
        term = input("Jaki termin mam usunąć?: ")
        if term in book:
            del book[term]
            print("\n", term, " został usunięty")
        else:
            print("Nie mogę tego zrobić! Słowa", term, "nie ma w słowniku")
