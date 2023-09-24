import json
import os

startpengar = int(500)
saldo = []


# -- FUNKTIONER FÖR JSON -- #
# Funktion för att hämta saldo.json om den finns annars
def hämta_saldo():
    if os.path.isfile("saldo.json"):
        with open("saldo.json", "r") as f:
            # Hämtar värde från saldo.json
            return json.load(f)
    # Finns ingen json returnerar vi värdet startpengar (500)
    return startpengar


# Funktion för att kolla stats.json
def hämta_stats():
    if os.path.isfile("stats.json"):
        with open("stats.json", "r") as f:
            # Hämtar värde från stats.json
            return json.load(f)
    # Skapar tom lista ifall stats.json ej finns
    return []


def hämta_regler():
    with open("regler.txt") as f:
        regler = f.read()
        return regler


# Funktion för att skriva till saldo.json
def spara_saldo(text):
    with open("saldo.json", "w+") as f:
        json.dump(text, f)


# Funktion för att skriva till stats.json
def spara_stats(text):
    with open("stats.json", "w+") as f:
        json.dump(text, f)
