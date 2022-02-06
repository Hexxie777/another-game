import random

print("""
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
       X   Witaj w grze papier, kamień, nożyce!   X
       X  Wybierz co chcesz zagrać i powodzenia!  X                    
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             
    """)
print("0 - Zakończenie rozgrywki\n1 - Papier\n2 - Kamień\n3 - Nożyce")

#Ilość wygranych rund
player_won = 0
pc_won = 0

player = None

def score():
    print("""
    
                SCOREBOARD
            
        """)
    print("         Masz ", player_won, "punktów")
    print("         Komputer ma ", pc_won, "punktów\n\n")
    print("0 - Zakończenie rozgrywki\n1 - Papier\n2 - Kamień\n3 - Nożyce")
while player != "0":
    
    player = input("Wpisz co chcesz zagrać: ")
    if player == "1":
        print("Zagrałeś papier")
        pc = random.randint(0,2)
        if pc == 0:
            print("Komputer zagrał papier\nRemis")
            score()
        elif pc == 1:
            print("Komputer zagrał kamień\nWygrałeś")
            player_won += 1
            score()
        elif pc == 2:
            print("Komputer zagrał nożyce\nPrzegrałeś")
            pc_won += 1
            score()
    elif player == "2":
        print("Zagrałeś kamień")
        pc = random.randint(0,2)
        if pc == 0:
            print("Komputer zagrał papier\nPrzegrałeś")
            pc_won += 1
            score()
        elif pc == 1:
            print("Komputer zagrał kamień\nRemis")
            score()
        elif pc == 2:
            print("Komputer zagrał nożyce\nWygrałeś")
            player_won += 1
            score()
    elif player == "3":
        print("Zagrałeś nożyce")
        pc = random.randint(0,2)
        if pc == 0:
            print("Komputer zagrał papier\nWygrałeś")
            player_won += 1
            score()
        elif pc == 1:
            print("Komputer zagrał kamień\nPrzegrałeś")
            pc_won += 1
            score()
        elif pc == 2:
            print("Komputer zagrał nożyce\nRemis")
            score()
    elif player == "0":
        print("""
        
            Zakończono grę.
        
        """)
        quit()
    else:
        print("Podano zły numer. Spróbuj ponownie.")
