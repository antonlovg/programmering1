# Spelet Tjugoett gjord av Anton Lövgren Repo: https://github.com/antonlovg/nackademin-demo/ Syftet med spelet är att
# komma närmst 21 men inte över, spelaren med högst valör i handen vinner, blir det lika så vinner datorn oavsett
# vilka kort man har. Ess räknas som 1 eller 14 och spelaren kan själv bestämma vad värdet ska vara på denna.
# Spelaren startar med 500kr om inget tidigare saldo finns.
# All stats och saldo från tidigare spelsession du spelet sparas i json-filer.
# Lycka till !

# Hämtar alla moduler vi använder oss av
# Döper om modulen Tjogoett_v3_json för att förenkla koden
import Tjugoett_v3_json as jsonData
import random
import ui
# Hämtar värdet ui_width från ui
from ui import ui_width

# Tomma listor med användarnas och datorns händer
spelare_hand = []
dator_hand = []

# Hämtar saldo och stats innan vi startar programmet
saldo = jsonData.hämta_saldo()
stats = jsonData.hämta_stats()


# -- KLASSER FÖR SPELET -- #
# Class för att ta med färg och valör till kort
class Kort:
    def __init__(self, färg, valör):
        self.färg = färg
        self.valör = valör


# Class för att hantera hela kortleken
class Kortlek:
    def __init__(self):
        # Tom lista där vi ska ha alla kort i
        self.kortlek = []
        # Hämtar skapa_kortlek samt blandar_kortlek när kortleken skapats
        self.skapa_kortlek()
        self.blandar_kortlek()

    # Skapar kortleken med färger och alla valörer
    def skapa_kortlek(self):
        färger = ['Hjärter', 'Ruter', 'Spader', 'Klöver']
        valörer = ['Ess', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knekt', 'Dam', 'Kung']

        # För att vi ska ha ett kort av varje valör så loopar vi igenom alla kombinationer
        # Slutar med att vi har 52 olika kort = en kortlek
        for färg in färger:
            for valör in valörer:
                kort = Kort(färg, valör)
                # För varje färg + valör kombination så appendar vi den till kortlek
                self.kortlek.append(kort)

    # Via random-modulen så blandar vi korten
    # https://www.w3schools.com/python/ref_random_shuffle.asp
    def blandar_kortlek(self):
        random.shuffle(self.kortlek)

    # Funktion för att dra ett kort från kortleken så vi kan spela spelt
    def dra_kort(self, hand):
        nytt_kort = self.kortlek.pop()
        # Kollar om kortet blev Ess, isåfall måste användaren avgöra om det ska vara 1 eller 14
        if nytt_kort.valör == 'Ess':
            kort_valör = ui.val("Du drog ett ess, ska det vara 1 eller 14?")
            if kort_valör == '1' or kort_valör == '14':
                nytt_kort.valör = kort_valör
            else:
                ui.val("Fel, du måste ange 1 eller 14")
        hand.append(nytt_kort)


# -- FUNKTIONER FÖR UI -- #
# Skriver ut utseendet på UI, tex rubrik
def meny(nuvarande_stats=False):
    ui.clear()
    ui.linjer()
    ui.title("TJUGOETT", "Anton Lövgren")
    ui.linjer()
    # Är nuvarande_stats inte satt till True så skriver vi inte ut stats
    if not nuvarande_stats:
        ui.övrigt(f"Saldo: {saldo}")
    # Är den True (se # Val 3) så byter vi ut Saldo till Stats
    if nuvarande_stats:
        ui.övrigt("Stats:".center(ui_width))
    ui.linjer()


# Skriver ut menyvalen
def menyval():
    ui.menyval("1", "Spela")
    ui.menyval("2", "Regler")
    ui.menyval("3", "Stats")
    ui.menyval("4", "Spara och avsluta")
    ui.linjer()


# Funktion för att spara stats & saldo när man tar detta val
def save_exit():
    meny()
    jsonData.spara_stats(stats)
    jsonData.spara_saldo(saldo)
    ui.övrigt("Tack för att du spelat!")
    ui.val("Vi har sparat ditt saldo och dina stats!")
    exit()


# -- FUNKTIONER FÖR KORTSPELET -- #
# Funktion för att kolla om användaren vill fortsätta med tidigare saldo eller börja om
def hantera_omstart(saldo):
    # Går bara in i loopen om saldot inte är 0
    if 0 < saldo != 0:
        while True:
            val_fortsätt = ui.val(
                f"Vill du börja om från 500kr eller fortsätta med ditt tidigare saldo som just nu är {saldo}kr? (fortsätt/omstart)").lower()
            ui.linjer()

            # Avbryter loopen direkt om användaren ej vill göra en omstart av saldo
            if val_fortsätt == "fortsätt":
                return saldo

            elif val_fortsätt == "omstart":

                # Hoppar in i en ny loop för att vara 100% säker att användaren vill återställa saldot
                while True:
                    riktigt_val_fortsätt = ui.val("Är du helt säker att du vill starta om? (j/n)").lower()

                    # Användaren har bestämt sig, återställer saldo och sparar det
                    if riktigt_val_fortsätt == "j":
                        saldo = jsonData.startpengar
                        jsonData.spara_saldo(saldo)
                        ui.linjer()
                        ui.val("Du har nu 500kr att använda dig av, tryck enter för att fortsätta")
                        return saldo

                    # Användaren ångrar sig, avbryter loopen utan åtgärd
                    elif riktigt_val_fortsätt == "n":
                        ui.val(f"Du har valt att ångra dig, du behåller ditt saldo på {saldo}kr")
                        return saldo

                    else:
                        ui.val("Ange ett riktigt val, tryck enter för att fortsätta")
            else:
                ui.val("Du angav inte ett korrekt val, tryck på enter för att försöka igen")

    # Finns inga pengar får användaren en startsumma direkt utan att behöva göra val
    else:
        saldo = jsonData.startpengar
        ui.övrigt("Du får nu 500kr att spela för, lycka till!")
        ui.val("Tryck enter för att fortsätta")
        return saldo


# Funktion där användaren får välja en insats att spela med
def välja_insats():
    ui.clear()
    meny()
    while True:
        satsa_pengar = ui.val(f"Ange din insats (max {saldo}kr)")

        # Kollar om användaren angett ett heltal
        try:
            satsa_pengar = int(satsa_pengar)

            # Kollar om heltalet är högre än noll men inte överskrider saldot man har
            if 0 < satsa_pengar <= saldo:
                satsa_pengar = int(satsa_pengar)
                return satsa_pengar

            else:
                ui.övrigt(f"Du har angett en felaktig summa, vänligen ange en summa mellan 1 och {saldo}")
                ui.val("Tryck enter för att försöka igen")

        except ValueError:
            ui.val("Ange ett heltal, tryck enter för att försöka igen")


# Grunden av spelet
def kolla_resultat(saldo, satsa_pengar, stats, spelare_summa, dator_hand, kortlek):
    # Har användaren dragit över 21 så är det förloust automatiskt
    if spelare_summa > 21:
        ui.övrigt(f"Du gick över 21 (du fick {spelare_summa} och därmed vinner datorn!)")
        # Tar bort summan användaren satsade
        saldo = saldo - satsa_pengar
        # Lägger in förlust i stats.json
        stats.append("Förlust")
        return saldo

    # Har användaren 21 eller under så börjar vi med datorns del
    else:
        # Låter datorn dra kort sålänge dens poäng är under 17
        while sum_kort_valörer(dator_hand) < 17:
            kortlek.dra_kort(dator_hand)

        # Beräknar totala summan datorn drar
        dator_summa = sum_kort_valörer(dator_hand)

        ui.clear()
        meny()
        ui.övrigt(f"Insats: {satsa_pengar}")
        ui.linjer()

        # Skriver ut vilka kort som datorn dragit
        for n in dator_hand:
            ui.övrigt(f"Datorn drar kort: {n.färg} {n.valör}")

        # Visar vilka kort spelaren har dragit
        ui.övrigt(f"Du har korten: {', '.join([f'{n.färg} {n.valör}' for n in spelare_hand])}, poäng: {spelare_summa}")
        ui.linjer()

        # Resultaten för alla scenarion där vi appendar Vinst eller Förlust beroende på resultat:

        # Har spelaren högre än datorn så vinner spelaren och får tillbaka sin insats + samma summa
        if dator_summa > 21 or spelare_summa > dator_summa:
            ui.övrigt(f"Grattis du fick {spelare_summa} medans datorn fick {dator_summa}, du vann!")
            saldo = saldo + satsa_pengar
            stats.append("Vinst")
        # Ovagjort räknas som förlust, dvs saldot minskas med summan man satsade
        elif spelare_summa == dator_summa:
            ui.övrigt(f"Ni båda fick {spelare_summa} och därmed har datorn vunnit, tyvärr!")
            saldo = saldo - satsa_pengar
            stats.append("Förlust")

        # Har datorn högre så har användaren förlorat, saldot minskas med summan man satsade
        else:
            ui.övrigt(f"Du fick {spelare_summa} och datorn fick {dator_summa}, tyvärr har du förlorat!")
            saldo = saldo - satsa_pengar
            stats.append("Förlust")

    return saldo


# Funktion för att beräkna summan av korten man har
def sum_kort_valörer(hand):
    # Skapar dictionary för att tilldela alla kort ett värde (Ess beräknas direkt när det dras då användaren får välja)
    # Detta görs då t.ex. Dam endast är en sträng och spelet ej vet vad det är värt
    valör_till_värde = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Knekt': 11,
                        'Dam': 12, 'Kung': 13}
    total_summa = 0

    # Går igenom varje kort
    for kort in hand:
        total_summa += valör_till_värde.get(kort.valör, 0)

    return total_summa


# -- FUNKTIONER FÖR VAL -- #
# Val 1 - Spela spelet (Del 1)
def starta_nytt_spel():
    # Sätter variable till global då åtkomst behövs utanför funktion också
    # https://www.w3schools.com/python/python_variables_global.asp
    global saldo

    # Hämtar funktionen hantera_omstart
    hantera_omstart(saldo)

    # Skapar ny kortlek via class vi gjorde tidigare
    kortlek = Kortlek()

    # Tomma listor för att hålla alla kort
    spelare_hand = []
    dator_hand = []

    # Hämtar funktionen välja_insats och tilldelar den
    satsa_pengar = välja_insats()

    # Låter användaren (spelare) dra kort först
    kortlek.dra_kort(spelare_hand)

    # Startar själva spelet (se Del 2)
    spelare_summa = spela_spelet(satsa_pengar, kortlek, spelare_hand)

    # Kollar resultatet som blev samt tilldelar det till saldo
    saldo = kolla_resultat(saldo, satsa_pengar, stats, spelare_summa, dator_hand, kortlek)

    # Sparar saldo och stats
    jsonData.spara_saldo(saldo)
    jsonData.spara_stats(stats)
    ui.linjer()
    ui.val("Tack för att du spelat, tryck enter för att gå tillbaka till menyn")


# Val 1 - Spela spelet (Del 2)
def spela_spelet(satsa_pengar, kortlek, spelare_hand):
    # Loop där användaren ska dra kort
    while True:
        ui.clear()
        meny()
        ui.övrigt(f"Insats: {satsa_pengar}")
        ui.linjer()

        # Beräknar spelarens summa och tilldelar den
        spelare_summa = sum_kort_valörer(spelare_hand)

        # Printar spelarens kort med en for-loop direkt i printen, join för att ha allt på samma rad
        # https://www.w3schools.com/python/ref_string_join.asp
        ui.övrigt(f"Du har korten: {', '.join([f'{n.färg} {n.valör}' for n in spelare_hand])}, poäng: {spelare_summa}")
        ui.linjer()

        # Kollar om spelaren har mer än 21 och avbryter loopen (> 21 är förust)
        if spelare_summa > 21:
            return spelare_summa

        # Avbryter loopen då 21 är det högsta man kan ha
        elif spelare_summa == 21:
            ui.övrigt("Grattis! Du har 21 poäng nu!")
            return spelare_summa

        # Kollar om användaren vill ha nytt kort, avbryter loopen om användaren ej vill
        else:
            val_dra_kort = ui.val("Vill du dra ett till kort (j/n)").lower()
            if val_dra_kort == "j":
                kortlek.dra_kort(spelare_hand)
            elif val_dra_kort == "n":
                return spelare_summa
            else:
                ui.val("Du behöver ange j eller n, tryck enter för att försöka igen")


# Val 2 - Regler
def visa_regler():
    ui.linjer()
    ui.övrigt(jsonData.hämta_regler())
    ui.linjer()
    ui.val("Tryck enter för att gå tillbaka till menyn")


# Val 3 - Spara stats
def visa_stats():
    # Hämtar andra varianten av meny-utseendet (Stats = True)
    meny(True)

    # Inga stats finns
    if not stats:
        ui.övrigt("Börja spela för att se dina stats här!")

    # Sätter en tom dictionary för att beräkna/lagra resultaten
    stats_resultat = {}

    # Loopar igenom stats om den finns och hämtar varje vinst/förlust
    for resultat in stats:
        if resultat in stats_resultat:
            stats_resultat[resultat] += 1
        else:
            stats_resultat[resultat] = 1

    # Printar förlust eller vinst
    for resultat, antal in stats_resultat.items():
        ui.övrigt(f"{resultat}: {antal}")

    # Om det finns sparade stats, kollar om användaren vill nollställa allt
    if stats:
        nollställa = ui.val("Vill du nollställa stats? (j/n)").lower()

        if nollställa == "j":
            # Kollar om användaren är 100% säker på att den vill nollställa
            riktigt_val_nollställa = ui.val("Är du säker på att du vill nollställa stats? (j/n). All resultat kommer att försvinna").lower()

            if riktigt_val_nollställa == "j":
                # Rensar listan
                # https://www.w3schools.com/python/ref_dictionary_clear.asp
                stats.clear()
                # Sparar den tomma listan
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


# -- PROGRAMMET -- #
while True:
    # UI
    meny()
    menyval()
    val = ui.val("Skriv ditt val")

    # Val 1 - Startar nytt spel
    if val == "1":
        starta_nytt_spel()

    # Val 2 - Hämtar regler.txt
    elif val == "2":
        visa_regler()

    # Val 3 - Visar tidigare stats
    elif val == "3":
        visa_stats()

    # Val 4 - Sparar och stänger spelet
    elif val == "4":
        save_exit()

    # Användaren skrev inte 1, 2, 3 eller 4
    else:
        ui.val("Du skrev inte ett korrekt val, tryck enter för att försöka igen...")
