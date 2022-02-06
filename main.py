#loginy do log
login = ["Worker", "Szef","Gość"]
#hasla do passw 
password = ["workspace", "imaboss", " "]

accounts = {"Worker" : "Pracownik", "Szef" : "Prezes", "Gość" : "Gościa"}
print("""
     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
     X  Witam w aplikacji firmy ''My tu ten bagno''!  X 
     X            Powoli się rozwijamy!!!             X
     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                
        
    """)


def games():
    print("Co chcesz włączyć?\n1 - 'Rock Papers Scissors'\n2 - 'Find a number'\n3 - Słownik")
    dec = int(input())
    if dec == 1:
        print("Włączam grę...")
        input("Naciśnij enter, aby kontynuować...")
        import games.game2 as rock_papers_scissors
    if dec == 2:
        print("Włączam grę...")
        input("Naciśnij enter, aby kontynuować...")
        import games.game1 as find_a_number
    if dec == 3:
        print("Ładuję słownik...")
        input("Naciśnij enter, aby kontynuować...")
        import games.slownik as slownik

log = input("Zaloguj się podając login: ")

passw = input("Podaj hasło: ")

if log == login[0] and passw == password[0]:
    print("Witaj ", login[0]," masz permisje: ",  accounts["Worker"])
    games()
elif log == login[1] and passw == password[1]:
    print("Witaj ",login[1], "masz permisje: ", accounts["Szef"])
    games()
elif log == login[2] and password[2]:
    print("Witaj ", login[2], " masz permisje: ", accounts["Gość"])
    games()
else:
    print("Podano złe dane.")
    