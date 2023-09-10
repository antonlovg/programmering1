import json
import os

ui_width = 30

# Startinsats
pengar = int(500)

# Skapar en fil
with open("Inlämningsuppgift/saldo_v2.json", "w+") as f:
    saldo = f.write(json.dumps(pengar))
with open("Inlämningsuppgift/stats_v2.json", "w+") as f:
    stats = f.write(json.dumps(f))

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
    print(f"| Saldo: {saldo}")
    print("-" * ui_width)
    print("| 1 |\tSpela")
    print("| 2 |\tSpara och avsluta")
    print("-" * ui_width)

    val = input("| > ")
    print("-" * ui_width)
    if val == "1":
        val_fortsätt = input(f"Vill du börja om från 500kr saldo\neller fortsätta med ditt saldo\nsom just nu är {saldo}kr?\n(continue/restart) > ").lower()
        if val_fortsätt == "continue":
            pengar = int(saldo)
        elif val_fortsätt == "restart":
            pengar = int(500)

    elif val == "2":
        print ("Val 2")
    else:
        print("Fel tecken")
    


    input("Test")
