# Spelet Tjugoett gjord av Anton Lövgren
# Repo: https://github.com/antonlovg/nackademin-demo/
# Syftet med spelet är att komma närmst 21 men inte över, spelaren med högst valör i handen vinner alternativt lika om man har samma valörer oavsett vilka kort man har.
# Ess räknas som 1 eller 14
# Spelaren startar med 500kr
# Lycka till !

import json
import os
import random

ui_width = 30

# Startinsats
startpengar = int(500)
stats = []

# Skapar en fil om den inte finns annars hämtar den info
if os.path.isfile("Inlämningsuppgift/saldo_v2.json"):
    with open("Inlämningsuppgift/saldo_v2.json", "r") as f:
        saldo = json.load(f)
else:
    saldo = startpengar

if os.path.isfile("Inlämningsuppgift/stats_v2.json"):
    try:
        with open("Inlämningsuppgift/stats_v2.json", "r") as f:
            stats = json.load(f)

    except json.JSONDecodeError:
        stats = []
else:
    stats = []

while True:
    # Rensar terminalen, nt = windows och posix = liux/mac
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    # UI
    print(".:  TJUGOETT  :.".center(ui_width))
    print("*" * ui_width)
    print("Gjord av Anton Lövgren".center(ui_width))
    print("*" * ui_width)
    print("| Har du inget saldo sen tidigare\n| så får du 500kr att spela med.")
    print("-" * ui_width)
    print(f"| Saldo: {saldo}")
    print("-" * ui_width)
    print("| 1 |\tSpela")
    print("| 2 |\tRegler")
    print("| 3 |\tStats")
    print("| 4 |\tSpara och avsluta")
    print("-" * ui_width)

    val = input("> ")
    print("-" * ui_width)
    if val == "1":
        if saldo > 0 and saldo != 0: 
            while True:
                if os.name == "nt":
                    os.system("cls")
                elif os.name == "posix":
                    os.system("clear")
                print(".:  TJUGOETT  :.".center(ui_width))
                print("*" * ui_width)
                print("Gjord av Anton Lövgren".center(ui_width))
                print("*" * ui_width)
                print(f"| Saldo: {saldo}")
                print("-" * ui_width)
                val_fortsätt = input(f"Vill du börja om från 500kr eller\nfortsätta med ditt tidigare saldo\nsom just nu är {saldo}kr?\n(continue/restart) > ").lower()
                print("-" * ui_width)
                if val_fortsätt == "continue":
                    input(f"Du valde att fortsätta, tryck enter for att gå vidare...")
                    break
                elif val_fortsätt == "restart":
                    riktigt_val_fortsätt = input("Är du helt säker att du vill starta om? (j/n) > ").lower()
                    if riktigt_val_fortsätt == "j":
                        saldo = startpengar
                        input("Du har nu 500kr att använda dig av, tryck enter för att fortsätta...")
                        break
                    elif riktigt_val_fortsätt == "n":
                        input(f"Du har valt att ångra dig, du behåller ditt saldo på {saldo}kr")
                        break
                    else:
                        input("1Ange ett riktigt val, tryck enter för att fortsätta...")
                else:
                    input("2Du angav inte ett korrekt val, tryck på enter för att försöka igen...")

        elif saldo < 0:
            saldo = startpengar
            input("Du får nu 500kr att spela för, lycka till!\nTryck enter för att fortsätta...")
        
        kort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        kortlek = kort * 4
        random.shuffle(kortlek)

        spelare_hand = []
        dator_hand = []
        
        while True:
            if os.name == "nt":
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")

            print(".:  TJUGOETT  :.".center(ui_width))
            print("*" * ui_width)
            print("Gjord av Anton Lövgren".center(ui_width))
            print("*" * ui_width)
            print(f"| Saldo: {saldo}")
            print("-" * ui_width)

            satsa_pengar = input(f"Ange din insats (max {saldo}kr) > ")
            print("-" * ui_width)
            try:
                satsa_pengar = int(satsa_pengar)
                satsa_pengar != 0
                break
            except ValueError:
                print(f"Du har angett en felaktig summa, vänligen\nange en summa mellan 1 och {saldo}")
        

        spelare_hand.append(kortlek.pop())

        while True:
            if os.name == "nt":
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")

            print(".:  TJUGOETT  :.".center(ui_width))
            print("*" * ui_width)
            print("Gjord av Anton Lövgren".center(ui_width))
            print("*" * ui_width)
            print(f"| Saldo: {saldo}")
            print(f"| Insats: {satsa_pengar}")
            print("-" * ui_width)

            spelare_summa = int(sum(spelare_hand))
            print(f"Du har korten: {spelare_hand}, poäng: {spelare_summa}")
            print("-" * ui_width)
            if spelare_summa > 21:
                print (f"Din hand är värd {spelare_summa} och överskred 21,\ntyvärr så har du förlorat!")
                break
            elif spelare_summa == 21:
                print("Blackjack! Du har 21 poäng nu!")
            else:
                dra_kort = input("Vill du dra ett till kort (j/n) > ").lower()
                if dra_kort == "j":
                    nytt_kort = kortlek.pop()
                    spelare_hand.append(nytt_kort)
                    print(f"Du fick kort {nytt_kort}!")
                elif dra_kort == "n":
                    break
                else:
                    input("Du behöver ange j eller n,\ntryck enter för att försöka igen...")
        
        while sum(dator_hand) < 17:
            dator_hand.append(kortlek.pop())
            
        dator_summa = int(sum(dator_hand))

        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        print(".:  TJUGOETT  :.".center(ui_width))
        print("*" * ui_width)
        print("Gjord av Anton Lövgren".center(ui_width))
        print("*" * ui_width)
        print(f"| Saldo: {saldo}")
        print(f"| Insats: {satsa_pengar}")
        print("-" * ui_width)
        print(f"Datorns kort är: {dator_hand}, poäng: {dator_summa}!")
        print("-" * ui_width)
        if spelare_summa > 21:
            print(f"Du gick över 21 (du fick {spelare_summa} och därmed vinner datorn!)")
            saldo = saldo - satsa_pengar
            stats.append("Vinst")
        elif dator_summa > 21 or spelare_summa > dator_summa:
            print(f"Grattis du fick {spelare_summa} medans datorn fick {dator_summa}, du vann!")
            saldo = saldo + satsa_pengar
            stats.append("Vinst")
        elif spelare_summa == dator_summa:
            print(f"Oavgjort, ni båda fick {spelare_summa}")
            stats.append("Oavgjort")
        else:
            print(f"Du fick {spelare_summa} och datorn fick {dator_summa}, tyvärr har du förlorat!")
            saldo = saldo - satsa_pengar
            stats.append("Förlust")
        
        with open("Inlämningsuppgift/saldo_v2.json", "w+") as f:
            json.dump(saldo, f)
        
        with open("Inlämningsuppgift/stats_v2.json", "w+") as f:
            json.dump(stats, f)
        
        köra_igen = input(" ")

    elif val == "2": # Regler , läs in från fil
        print("val 2")
    elif val == "3": # Stats
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

        print(".:  TJUGOETT  :.".center(ui_width))
        print("*" * ui_width)
        print("Gjord av Anton Lövgren".center(ui_width))
        print("*" * ui_width)
        print("  STATS:  ".center(ui_width))
        print("-" * ui_width)

        if not stats:
            print("| Börja spela för att se dina stats här!")

        stats_resultat = {}

        for resultat in stats:
            if resultat in stats_resultat:
                stats_resultat[resultat] += 1
            else:
                stats_resultat[resultat] = 1
        for resultat, antal in stats_resultat.items():
            print(f"| {resultat}: {antal}")

        print("-" * ui_width)
        if stats:
            nollställa = input("Vill du nollställa stats? (j/n) > ").lower()
            if nollställa == "j":
                riktigt_val_nollställa = input("Är du säker på att du vill nollställa stats? (j/n)\nAll resultat kommer att försvinna > ").lower()
                if riktigt_val_nollställa == "j":
                    stats.clear()
                    
                    with open("Inlämningsuppgift/stats_v2.json", "w+") as f:
                        json.dump(stats, f)
                    
                    input("Stats nollställts, tryck enter för att fortsätta...")
                elif riktigt_val_nollställa == "n":
                    input("Tidigare stats är kvar, inget har nollställts, enter för att fortsätta...")
                else:
                    input("Felaktigt val, tryck enter för att försöka igen...")
            elif nollställa == "n":
                input("Inget har nollställts, tryck enter för att gå tillbaka till menyn")
            else:
                input("ERROR: Felaktigt val, tryck enter för gå vidare...")
        input("Tryck enter för att gå tillbaka till menyn...")

    elif val == "4": # Spara o avsluta
        print("Val 4")
    else:
        input("ERROR: Du har angett fel tecken,\ntryck enter för att försöka igen...")
    

    
input("yo test")
    


input("Test")

#Förlorat = förlust
#Vinst = vinst
#Oavgjort = oavgjort