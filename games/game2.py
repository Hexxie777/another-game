import random

#'Losowanie' liczby 1 - papier 2 - kamien - nozyce
pc = random.randint(1,3)

print("""
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
       X   Witaj w grze papier, kamień, nożyce!   X
       X  Wybierz co chcesz zagrać i powodzenia!  X                    
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             
    """)
print("0 - Zakończenie rozgrywki\n1 - Papier\n2 - Kamień\n3 - Nożyce")

player_won = 0

pc_won = 0

player = None

pc_pick = None

def score(pc_pick):
    print("""
    
                SCOREBOARD
            
        """)
    print("         Masz ", player_won, "punktów")
    print("         Komputer ma ", pc_won, "punktów\n\n")

while player != "4":
    
    
    
    player = input("Wpisz co chcesz zagrać: ")
    if player == "1":
        
        print("Zagrałeś papier")
        pc = random.randint(0,2)
        if pc == 0:
            print("Komputer zagrał papier\nRemis")
            score(pc_pick)
        elif pc == 1:
            print("Komputer zagrał kamień\nWygrałeś")
            player_won += 1
            score(pc_pick)
        elif pc == 2:
            print("Komputer zagrał nożyce\nPrzegrałeś")
            pc_won += 1
            score(pc_pick)
    elif player == "2":
        print("Zagrałeś kamień")
        pc = random.randint(0,2)
        if pc == 0:
            print("Komputer zagrał papier\nPrzegrałeś")
            pc_won += 1
            score(pc_pick)
        elif pc == 1:
            print("Komputer zagrał kamień\nRemis")
            score(pc_pick)
        elif pc == 2:
            print("Komputer zagrał nożyce\nWygrałeś")
            player_won += 1
            score(pc_pick)
    elif player == "3":
        print("Zagrałeś nożyce")
        pc = random.randint(0,2)
        if pc == 0:
            print("Komputer zagrał papier\nWygrałeś")
            player_won += 1
            score(pc_pick)
        elif pc == 1:
            print("Komputer zagrał kamień\nPrzegrałeś")
            pc_won += 1
            score(pc_pick)
        elif pc == 2:
            print("Komputer zagrał nożyce\nRemis")
            score(pc_pick)
    elif player == "0":
        print("Zakończono grę")
        quit()
        
        