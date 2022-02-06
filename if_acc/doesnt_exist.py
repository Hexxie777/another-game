#Wybór gry
def games():
    
    print("Co chcesz włączyć?\n1 - 'Rock Papers Scissors'\n2 - 'Find a number'\n3 - Słownik")
    dec = input(">>> ")    
    while dec != "1" or "2" or "3":
        if dec == "1":
            print("Włączam grę:'Papier kamień nożyce'...")
            input("Naciśnij enter, aby kontynuować...")
            import games.game2 as rock_papers_scissors
        if dec == "2":
            print("Włączam grę:'Jaka to liczba'...")
            input("Naciśnij enter, aby kontynuować...")
            import games.game1 as find_a_number
        if dec == "3":
            print("Ładuję słownik...")
            input("Naciśnij enter, aby kontynuować...")
            import games.slownik as slownik
        else:
            print("Podano zły warunek. Spróbuj ponownie. ")
            dec = input(">>> ")


login = []
password = []

print("Podaj nowy login i hasło.")

#Rejstracja
new_login = input("Login: ")
new_password = input("Hasło: ")

#Dodawanie danych 
login.append(new_login)
password.append(new_password)

print("Teraz możesz zalogować się do aplikacji, podaj dane: ")

#Logowanie się z "nowego konta"
while True:
    app_login = input("Podaj login: ")
    app_password = input("Podaj hasło: ")
    if app_login == login[0] and app_password == password[0]:
        print("Witaj", login[0], "narazie masz permisje gościa, poczekaj na zweryfikowanie swojego konta.")
        games()
    else:
        print("Podano złe dane. Spróbuj ponownie.")

