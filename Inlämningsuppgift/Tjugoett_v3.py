# Spelet Tjugoett gjord av Anton Lövgren Repo: https://github.com/antonlovg/nackademin-demo/ Syftet med spelet är att
# komma närmst 21 men inte över, spelaren med högst valör i handen vinner, blir det lika så vinner datorn oavsett
# vilka kort man har. Ess räknas som 1 eller 14 och spelaren kan själv bestämma vad värdet ska vara på denna.
# Spelaren startar med 500kr om inget tidigare saldo finns.
# Lycka till !

# Hämtar alla moduler vi använder oss av
# import json
import Tjugoett_v3_json as jsonData
import random
# import os
import ui
from ui import ui_width


# -- FUNKTIONER -- #
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


# Tomma listor med användarnas och datorns händer
spelare_hand = []
dator_hand = []

saldo = jsonData.hämta_saldo()
stats = jsonData.hämta_stats()

# -- PROGRAMMET -- #
while True:
    # UI
    meny()
    menyval()
    val = ui.val("Skriv ditt val")

    if val == "1":
        if val == "1":
            if 0 < saldo != 0:  # Kollar om det finns pengar kvar att använda, annars hoppar den över denna
                # del

                # Denna while-loop kollar om användaren vill använda tidigare saldo eller börja från nytt
                while True:

                    ui.clear()
                    meny()

                    # Sätter .lower() i slutet för att undvika problem om användaren skriver CONTINUE eller Continue
                    # Kommer göra det på flera ställen när det är ett val/input
                    val_fortsätt = ui.val(f"Vill du börja om från 500kr eller fortsätta med ditt tidigare saldo som "
                                          f"just nu är {saldo}kr? (continue/restart)").lower()
                    ui.linjer()
                    # Vi hoppar in i if-satsen om användaren valt continue och då möter vi break som slänger ut oss ur
                    # while-loopen (men bara den som kollar saldo)
                    if val_fortsätt == "continue":
                        break
                    # Else-if om man väljer restart, har även en extra check ifall användaren är 100% säker på att den
                    # vill starta från startpengar (500kr) Samma sak också, .lower() så användaren inte behöver tänka på
                    # hur den skriver
                    elif val_fortsätt == "restart":
                        riktigt_val_fortsätt = ui.val("Är du helt säker att du vill starta om? (j/n)").lower()
                        if riktigt_val_fortsätt == "j":
                            saldo = jsonData.startpengar
                            ui.linjer()
                            ui.val("Du har nu 500kr att använda dig av, tryck enter för att fortsätta")
                            break
                        elif riktigt_val_fortsätt == "n":
                            ui.val(f"Du har valt att ångra dig, du behåller ditt saldo på {saldo}kr")
                            break
                        # Dessa två else är om användaren skrivit fel, då hoppar vi tillbaka till starten av denna
                        # saldo-while-loop
                        else:
                            ui.val("Ange ett riktigt val, tryck enter för att fortsätta")
                    else:
                        ui.val("Du angav inte ett korrekt val, tryck på enter för att försöka igen")

            else:  # Finns inga pengar får användaren en startsumma direkt utan att behöva göra val
                saldo = jsonData.startpengar
                ui.övrigt("Du får nu 500kr att spela för, lycka till!")
                ui.val("Tryck enter för att fortsätta")

            kort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Detta är alla värden som vi har i en kortlek. Vi vill
            # att 1 (ess) ska kunna bli 14 men ENDAST
            # om man inte går över 21 och detta kollar vi med en if-sats senare.

            kortlek = kort * 4  # Detta gör vi eftersom varje valör finns med fyra exemplar dvs 52 kort totalt i en
            # kortlek.

            random.shuffle(kortlek)  # Precis som vi skulle blanda korten för hand så gör vi detta med shuffle,
            # nu ligger listan i
            # en slumpmässig ordning med fyra st exemplar av varje valör

            # Tomma listor med användarnas och datorns händer
            spelare_hand = []
            dator_hand = []

            while True:
                ui.clear()
                meny()
                satsa_pengar = ui.val(f"Ange din insats (max {saldo}kr)")
                ui.linjer()

                try:
                    satsa_pengar = int(satsa_pengar)
                    if 0 < satsa_pengar <= saldo:
                        satsa_pengar = int(satsa_pengar)
                        break

                    else:
                        ui.övrigt(f"Du har angett en felaktig summa, vänligen ange en summa mellan 1 och {saldo}")
                        ui.val("Tryck enter för att försöka igen")

                except ValueError:
                    ui.val("Ange ett heltal")

            spelare_hand.append(kortlek.pop())

            while True:
                ui.clear()
                meny()
                ui.övrigt(f"Insats: {satsa_pengar}")
                ui.linjer()

                spelare_summa = int(sum(spelare_hand))
                ui.övrigt(f"Du har korten: {spelare_hand}, poäng: {spelare_summa}")
                ui.linjer()

                if spelare_summa > 21:
                    break

                elif spelare_summa == 21:
                    ui.övrigt("Blackjack! Du har 21 poäng nu!")

                else:
                    dra_kort = ui.val("Vill du dra ett till kort (j/n)").lower()
                    if dra_kort == "j":
                        nytt_kort = kortlek.pop()
                        spelare_hand.append(nytt_kort)
                        ui.övrigt(f"Du fick kort {nytt_kort}!")
                    elif dra_kort == "n":
                        break
                    else:
                        ui.val("Du behöver ange j eller n,\ntryck enter för att försöka igen")

            if spelare_summa > 21:
                ui.övrigt(f"Du gick över 21 (du fick {spelare_summa} och därmed vinner datorn!)")
                saldo = saldo - satsa_pengar
                stats.append("Förlust")

            else:
                while sum(dator_hand) < 17:
                    dator_hand.append(kortlek.pop())

                dator_summa = int(sum(dator_hand))

                ui.clear()
                meny()
                ui.övrigt(f"| Insats: {satsa_pengar}")
                ui.linjer()

                for n in dator_hand:
                    ui.övrigt(f"Datorn drar kort: {n}")

                ui.övrigt(f"Datorns kort är: {dator_hand}, poäng: {dator_summa}!")
                ui.linjer()

                if dator_summa > 21 or spelare_summa > dator_summa:
                    ui.övrigt(f"Grattis du fick {spelare_summa} medans datorn fick {dator_summa}, du vann!")
                    saldo = saldo + satsa_pengar
                    stats.append("Vinst")

                elif spelare_summa == dator_summa:
                    ui.övrigt(f"Ni båda fick {spelare_summa} och därmed har datorn vunnit, tyvärr!")
                    stats.append("Förlust")

                else:
                    ui.övrigt(f"Du fick {spelare_summa} och datorn fick {dator_summa}, tyvärr har du förlorat!")
                    saldo = saldo - satsa_pengar
                    stats.append("Förlust")

            jsonData.spara_saldo(saldo)
            jsonData.spara_stats(stats)
            ui.linjer()
            ui.val("Tack för att du spelat, tryck enter för att gå tillbaka till menyn")

    elif val == "2":
        meny()
        ui.övrigt("Vinn, förlora inte!")
    elif val == "3":
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

        ui.val("Tryck enter för att gå tillbaka till menyn")

    elif val == "4":
        save_exit()
    else:
        ui.val("Du skrev inte ett korrekt val, tryck enter för att försöka igen...")
