# Code Challenge Sten-sax-påse

import getpass
import random
import time

vapen = [ "sten", "sax", "påse"]

p1_score = 0
p2_score = 0

def player_input(text):
    """Tar emot spelarens val av vapen"""
    while True:
        try:
            #inp = int(getpass.getpass(text))
            inp = int(input(text))
            vapen[inp-1] # Denna rad orsakar IndexError vid behov
            return inp
        except ValueError:
            print("Skriv ett heltal.")
        except IndexError:
            print("Finns inget sådant vapen.")
            
while True:

    print("-- Skriv 1, 2 eller 3:")
    for i, v in enumerate(vapen):
        print(f"{i+1} - {v}")

    p1 = player_input("Spelare 1: ")
    #p2 = player_input("Spelare 2: ")
    p2 = random.randint(1, 3)
    
    time.sleep(1) # Vänta en sekund...

    print(f"Spelare 2: {p2}")
    print(f"{vapen[p1-1]} mot {vapen[p2-1]}...")

    if p1 == p2:
        print("Jämnt spel!")

    elif ( (p1 == 1 and p2 == 2) 
        or (p1 == 2 and p2 == 3) 
        or (p1 == 3 and p2 == 1)):
            
        print("Spelare 1 vinner!")
        p1_score += 1

    else:
        print("Spelare 2 vinner!")
        p2_score += 1

    print(f"Ställningen är (spelare 1 mot spelare 2): {p1_score} - {p2_score}")

    if input("Spela igen? Y/n: ").lower() == "n":
        print("Tack o hej")
        break




    

