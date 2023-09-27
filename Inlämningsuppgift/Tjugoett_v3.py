# Spelet Tjugoett gjord av Anton Lövgren Repo: https://github.com/antonlovg/nackademin-demo/ Syftet med spelet är att
# komma närmst 21 men inte över, spelaren med högst valör i handen vinner, blir det lika så vinner datorn oavsett
# vilka kort man har. Ess räknas som 1 eller 14 och spelaren kan själv bestämma vad värdet ska vara på denna.
# Spelaren startar med 500kr om inget tidigare saldo finns.
# Lycka till !

# Hämtar alla moduler vi använder oss av
import Tjugoett_v3_json as jsonData
import random
import ui
from ui import ui_width

# Tomma listor med användarnas och datorns händer
spelare_hand = []
dator_hand = []


# -- KLASSER FÖR SPELET -- #
# Class för att ta med färg och valör till kort
class Kort:
    def __init__(self, färg, valör):
        self.färg = färg
        self.valör = valör


# Class för att hantera hela kortleken
class Kortlek:
    def __init__(self):
        self.kortlek = []
        self.skapa_kortlek()
        self.blandar_kortlek()

    def skapa_kortlek(self):
        färger = ['Hjärter', 'Ruter', 'Spader', 'Klöver']
        valörer = ['Ess', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knekt', 'Dam', 'Kung']

        for färg in färger:
            for valör in valörer:
                kort = Kort(färg, valör)
                self.kortlek.append(kort)

    def blandar_kortlek(self):
        random.shuffle(self.kortlek)

    def dra_kort(self, hand):
        nytt_kort = self.kortlek.pop()
        if nytt_kort.valör == 'Ess':
            kort_valör = ui.val("Du drog ett ess, ska det vara 1 eller 14?")
            if kort_valör == '1' or kort_valör == '14':
                nytt_kort.valör = kort_valör
            else:
                ui.val("Fel, du måste ange 1 eller 14")
        hand.append(nytt_kort)


# -- FUNKTIONER FÖR UI -- #
def meny(nuvarande_stats=False):
    ui.clear()
    ui.linjer()
    ui.title("TJUGOETT", "Anton Lövgren")
    ui.linjer()
    if not nuvarande_stats:
        ui.övrigt(f"Saldo: {saldo}")
    if nuvarande_stats:
        ui.övrigt("Stats:".center(ui_width))
    ui.linjer()


def menyval():
    ui.menyval("1", "Spela")
    ui.menyval("2", "Regler")
    ui.menyval("3", "Stats")
    ui.menyval("4", "Spara och avsluta")
    ui.linjer()


def save_exit():
    meny()
    jsonData.spara_stats(stats)
    jsonData.spara_saldo(saldo)
    ui.övrigt("Tack för att du spelat!")
    ui.val("Vi har sparat ditt saldo och dina stats!")
    exit()


# -- FUNKTIONER FÖR KORTSPELET -- #
# Tar fram alla kort i en kortlek
def hantera_omstart(saldo):
    if 0 < saldo != 0:
        while True:
            val_fortsätt = ui.val(
                f"Vill du börja om från 500kr eller fortsätta med ditt tidigare saldo som just nu är {saldo}kr? (continue/restart)").lower()
            ui.linjer()
            if val_fortsätt == "continue":
                break

            elif val_fortsätt == "restart":
                while True:
                    riktigt_val_fortsätt = ui.val("Är du helt säker att du vill starta om? (j/n)").lower()

                    if riktigt_val_fortsätt == "j":
                        saldo = jsonData.startpengar
                        jsonData.spara_saldo(saldo)
                        ui.linjer()
                        ui.val("Du har nu 500kr att använda dig av, tryck enter för att fortsätta")
                        return saldo

                    elif riktigt_val_fortsätt == "n":
                        ui.val(f"Du har valt att ångra dig, du behåller ditt saldo på {saldo}kr")
                        return saldo

                    else:
                        ui.val("Ange ett riktigt val, tryck enter för att fortsätta")
            else:
                ui.val("Du angav inte ett korrekt val, tryck på enter för att försöka igen")

    else:  # Finns inga pengar får användaren en startsumma direkt utan att behöva göra val
        saldo = jsonData.startpengar
        ui.övrigt("Du får nu 500kr att spela för, lycka till!")
        ui.val("Tryck enter för att fortsätta")
        return saldo


def välja_insats():
    ui.clear()
    meny()
    while True:
        satsa_pengar = ui.val(f"Ange din insats (max {saldo}kr)")
        try:
            satsa_pengar = int(satsa_pengar)
            if 0 < satsa_pengar <= saldo:
                satsa_pengar = int(satsa_pengar)
                return satsa_pengar

            else:
                ui.övrigt(f"Du har angett en felaktig summa, vänligen ange en summa mellan 1 och {saldo}")
                ui.val("Tryck enter för att försöka igen")

        except ValueError:
            ui.val("Ange ett heltal, tryck enter för att försöka igen")


def kolla_resultat(saldo, satsa_pengar, stats, spelare_summa, dator_hand, kortlek):
    if spelare_summa > 21:
        ui.övrigt(f"Du gick över 21 (du fick {spelare_summa} och därmed vinner datorn!)")
        saldo = saldo - satsa_pengar
        stats.append("Förlust")
        return saldo

    else:
        while sum_kort_valörer(dator_hand) < 17:
            kortlek.dra_kort(dator_hand)

        dator_summa = sum_kort_valörer(dator_hand)

        ui.clear()
        meny()
        ui.övrigt(f"Insats: {satsa_pengar}")
        ui.linjer()

        for n in dator_hand:
            ui.övrigt(f"Datorn drar kort: {n.färg} {n.valör}")

        ui.övrigt(f"Du har korten: {', '.join([f'{n.färg} {n.valör}' for n in spelare_hand])}, poäng: {spelare_summa}")
        ui.linjer()

        if dator_summa > 21 or spelare_summa > dator_summa:
            ui.övrigt(f"Grattis du fick {spelare_summa} medans datorn fick {dator_summa}, du vann!")
            saldo = saldo + satsa_pengar
            stats.append("Vinst")

        elif spelare_summa == dator_summa:
            ui.övrigt(f"Ni båda fick {spelare_summa} och därmed har datorn vunnit, tyvärr!")
            saldo = saldo - satsa_pengar
            stats.append("Förlust")

        else:
            ui.övrigt(f"Du fick {spelare_summa} och datorn fick {dator_summa}, tyvärr har du förlorat!")
            saldo = saldo - satsa_pengar
            stats.append("Förlust")

    return saldo


def sum_kort_valörer(hand):
    valör_till_värde = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Knekt': 11,
                        'Dam': 12, 'Kung': 13}
    total_summa = 0

    for kort in hand:
        total_summa += valör_till_värde.get(kort.valör, 0)

    return total_summa


# -- FUNKTIONER FÖR VAL -- #
# Val 1 - Spela spelet (Del 1)
def spela_spelet(satsa_pengar, kortlek, spelare_hand):
    while True:
        ui.clear()
        meny()
        ui.övrigt(f"Insats: {satsa_pengar}")
        ui.linjer()

        spelare_summa = sum_kort_valörer(spelare_hand)

        ui.övrigt(f"Du har korten: {', '.join([f'{n.färg} {n.valör}' for n in spelare_hand])}, poäng: {spelare_summa}")
        ui.linjer()

        if spelare_summa > 21:
            return spelare_summa

        elif spelare_summa == 21:
            ui.övrigt("Grattis! Du har 21 poäng nu!")
            return spelare_summa

        else:
            val_dra_kort = ui.val("Vill du dra ett till kort (j/n)").lower()
            if val_dra_kort == "j":
                kortlek.dra_kort(spelare_hand)
            elif val_dra_kort == "n":
                return spelare_summa
            else:
                ui.val("Du behöver ange j eller n, tryck enter för att försöka igen")


# Val 1 - Spela spelet (Del 2)
def starta_nytt_spel():
    global saldo
    hantera_omstart(saldo)

    kortlek = Kortlek()

    spelare_hand = []
    dator_hand = []

    satsa_pengar = välja_insats()

    kortlek.dra_kort(spelare_hand)

    spelare_summa = spela_spelet(satsa_pengar, kortlek, spelare_hand)
    saldo = kolla_resultat(saldo, satsa_pengar, stats, spelare_summa, dator_hand, kortlek)

    jsonData.spara_saldo(saldo)
    jsonData.spara_stats(stats)
    ui.linjer()
    ui.val("Tack för att du spelat, tryck enter för att gå tillbaka till menyn")


# Val 2 - Regler
def visa_regler():
    ui.linjer()
    ui.övrigt(jsonData.hämta_regler())
    ui.linjer()
    ui.val("Tryck enter för att gå tillbaka till menyn")


# Val 3 - Spara stats
def visa_stats():
    meny(True)
    if not stats:
        ui.övrigt("Börja spela för att se dina stats här!")

    stats_resultat = {}

    for resultat in stats:
        if resultat in stats_resultat:
            stats_resultat[resultat] += 1
        else:
            stats_resultat[resultat] = 1
    for resultat, antal in stats_resultat.items():
        ui.övrigt(f"{resultat}: {antal}")

    if stats:
        nollställa = ui.val("Vill du nollställa stats? (j/n)").lower()
        if nollställa == "j":
            riktigt_val_nollställa = ui.val(
                "Är du säker på att du vill nollställa stats? (j/n). All resultat kommer att försvinna").lower()
            if riktigt_val_nollställa == "j":
                stats.clear()
                jsonData.spara_stats(stats)

                ui.val("Stats nollställts, tryck enter för att fortsätta")

            elif riktigt_val_nollställa == "n":
                ui.val("Tidigare stats är kvar, inget har nollställts, enter för att fortsätta")

            else:
                ui.val("Felaktigt val, tryck enter för att försöka igen")

        elif nollställa == "n":
            ui.val("Inget har nollställts, tryck enter för att gå tillbaka till menyn")

        else:
            ui.val("ERROR: Felaktigt val, tryck enter för gå vidare")


saldo = jsonData.hämta_saldo()
stats = jsonData.hämta_stats()

# -- PROGRAMMET -- #
while True:
    # UI
    meny()
    menyval()
    val = ui.val("Skriv ditt val")

    if val == "1":
        starta_nytt_spel()

    elif val == "2":
        visa_regler()

    elif val == "3":
        visa_stats()

    elif val == "4":
        save_exit()

    else:
        ui.val("Du skrev inte ett korrekt val, tryck enter för att försöka igen...")
