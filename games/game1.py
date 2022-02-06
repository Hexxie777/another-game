import random

#Generowanie liczby
number = random.randint(1,100)

tries = 0

print("""
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    X   Witaj w grze jaka to liczba! Musisz zgadąć liczbę wygenerowaną przez komputer  X
    X                       (od 0 do 100), masz tylko 10 prób!                         X
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

      """
)

while True:
    #Pozostałe próby
    print("Pozostało ", 10 - tries, "prób.")
    
    guess = int(input("\nPodaj liczbę: "))

    if tries == 9:
        print("""           
        
        
                      GAME OVER
        
        
                """)
        break
   
    if guess == number:
        print("""
        
                    <-!-> YOU WON <-!->    

                """)
        print(number, "to dobra liczba!","\nWykorzystałeś", tries, "prób")        
        break
    
    if guess <= number:
        tries += 1
        print("Nie udało Ci się, podana liczba jest za mała...\n")
    
    elif guess >= number:
        tries += 1
        print("Nie udało Ci się, podana liczba jest za duża...\n")