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

if not os.path.isfile("Inlämningsuppgift/stats_v2.json"):
    with open("Inlämningsuppgift/stats_v2.json", "w+") as f:
        stats = f.write(json.dumps(stats))

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
    print("| Har du inget saldo sen tidigare\n| så får du 500kr att\n| spela med.")
    print("-" * ui_width)
    print(f"| Saldo: {saldo}")
    print("-" * ui_width)
    print("| 1 |\tSpela")
    print("| 2 |\tRegler")
    print("| 3 |\tSpara och avsluta")
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
        elif dator_summa > 21 or spelare_summa > dator_summa:
            print(f"Grattis du fick {spelare_summa} medans datorn fick {dator_summa}, du vann!")
            saldo = saldo + satsa_pengar
        elif spelare_summa == dator_summa:
            print(f"Oavgjort, ni båda fick {spelare_summa}")
        else:
            print(f"Du fick {spelare_summa} och datorn fick {dator_summa}, tyvärr har du förlorat!")
            saldo = saldo - satsa_pengar
            stats.append("Förlust")
        
        with open("Inlämningsuppgift/saldo_v2.json", "r") as f:
            saldo = json.load(f)
        
        köra_igen = input("")

    elif val == "2":
        print("val 2")
    elif val == "3":
        print("Val 3")
    else:
        print("Fel tecken")
    input("yo test")
    


    input("Test")

#Förlorat = Förlust