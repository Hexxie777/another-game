import random

#'Losowanie' liczby
pc = random.randint(1,3)

print("""
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
       X   Witaj w grze papier, kamień, nożyce!   X
       X  Wybierz co chcesz zagrać i powodzenia!  X                    
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             
    """)
print("1 - Papier\n2 - Kamień\n3 - Nożyce\n4 - Zakończenie gry")


player = None

#Komputer zagrał papier
def win(pc):   
    if pc == 1:
        print("Komputer zagrał papier\nRemis")
    elif pc == 2:
        print("Komputer zagrał kamień\nWygrałeś")
    elif pc == 3:
        print("Komputer zagrał nożyce\nPrzegrałeś")
#Komputer zagrał kamień
def win1(pc):
    if pc == 1:
        print("Komputer zagrał papier\nPrzegrałeś")
    elif pc == 2:
        print("Komputer zagrał kamień\nRemis")
    elif pc == 3:
        print("Komputer zagrał nożyce\nWygrałeś")
#Komputer zagrał nożyce
def win2(pc):
    if pc == 1:
        print("Komputer zagrał papier\nWygrałeś")
    elif pc == 2:
        print("Komputer zagrał kamień\nPrzegrałeś")
    elif pc == 3:
        print("Komputer zagrał nożyce\nRemis")


while player != "4":
    player = input("Wpisz co chcesz zagrać: ")
    if player == "1":
        print("Zagrałeś papier")
        win(pc)
        pc = random.randint(1,3)    
    elif player == "2":
        print("Zagrałeś kamień")
        win1(pc)
        pc = random.randint(1,3)
    elif player == "3":
        print("Zagrałeś nożyce")
        win2(pc)
        pc = random.randint(1,3)
    elif player == "4":
        print("Zakończono grę")