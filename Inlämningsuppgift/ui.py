# UI-modul
import os

ui_width = 30


def linjer():
    print("-" * ui_width)


def title(text1, text2):
    print(".:".ljust(5), text1.center(20), ":.".rjust(4))
    print(".:".ljust(5), text2.center(20), ":.".rjust(4))


def val(text):
    return input("| " + text + " > ")


def clear():
    if os.name == "nt":
        os.system("cls")

    elif os.name == "posix":
        os.system("clear")


def menyval(text1, text2):
    print("|", text1, f"|\t{text2}")


def övrigt(text):
    print("| " + text)
