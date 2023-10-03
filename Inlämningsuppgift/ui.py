# UI-modul
import os

ui_width = 30


# Skapar linjer
def linjer():
    print("-" * ui_width)


# Skapar title
def title(text1, text2):
    print("|".ljust(5), text1.center(20), "|".rjust(3))
    print("|".ljust(5), text2.center(20), "|".rjust(3))


# Skapar valmöjligheter
def val(text):
    return input("| " + text + " > ")


# Rensar terminalen
def clear():
    if os.name == "nt":
        os.system("cls")

    elif os.name == "posix":
        os.system("clear")


# Skapar utseende för val
def menyval(text1, text2):
    print("|", text1, f"|\t{text2}")


# Alla övrigt som behöver skrivas ut
def övrigt(text):
    print("| " + text)
