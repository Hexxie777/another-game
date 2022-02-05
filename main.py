#loginy do log
login = ["Worker", "Szef","Gość"]
#hasla do passw przy gosciu kliknij enter
password = ["workspace", "imaboss", " "]

accounts = {"Worker" : "Pracownik", "Szef" : "Prezes", "Gość" : "Gościa"}
print("""
     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
     X  Witam w aplikacji firmy ''My tu ten bagno''!  X 
     X            Powoli się rozwijamy!!!             X
     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                
        
    """)

log = input("Zaloguj się podając login: ")

passw = input("Podaj hasło: ")

if log == login[0] and passw == password[0]:
    print("Witaj ", login[0]," masz permisje: ",  accounts["Grzegorz"])
    print("Masz dużo roboty, zrobisz coś pożytecznego co?")
    #Importowanie gry w zależności od podanego konta
    import games.game2 as game2
elif log == login[1] and passw == password[1]:
    print("Witaj ",login[1], "ty tu jesteś szefem B)")
    print("Baw się dobrze!")
    #Importowanie gry w zależności od podanego konta
    import games.game1 as game1
elif log == login[2] and password[2]:
    print("Witaj ", login[2], " masz permisje: ", accounts["Gość"])
    print("A co tu takiego ciekawego?")
    #Importowanie gry w zależności od podanego konta
    import games.slownik as slownik
else:
    print("Podano złe dane")
    