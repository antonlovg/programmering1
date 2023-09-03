# Spelet Tjugoett gjord av Anton Lövgren
# Syftet med spelet är att komma närmst 21 men inte över, spelaren med högst valör i handen vinner alternativt lika om man har samma valörer oavsett vilka kort man har.
# Ess räknas som 1 eller 14
# Spelaren startar med 500kr

import random # Importar modulen som heter random (tidigare använt i lektion 3) som gör att vi kan ta fram slumpmässiga kort.

while True:

    # Startinsant
    pengar = 500

    # Kortleken
    kort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # Detta är alla värden som vi har i en kortlek. Vi vill att 1 (ess) ska kunna bli 14 men ENDAST om man inte går över 21 och detta kollar vi med en if-sats.
    kortlek = kort * 4 # Detta gör vi eftersom varje valör finns med fyra exemplar dvs 52 kort totalt.
    random.shuffle(kortlek) # Precis som vi skulle blanda korten för hand så gör vi detta med shuffle, nu ligger listan i en slumpmässig ordning med fyra st exemplar av varje valör

    # Tomma istor med användarens och datorns hand
    spelareHand = []
    datorHand = []

    # Eftersom spelaren ska ha två kort innan den får bestämma om den vill dra mer kort så måste vi tilldela den det:
    # kortlek.pop() = kortlek.pop()     # Append används för att lägga till ett värde i en lista men vi vill bara ta ett nummer från kortlek-listan
    spelareHand.append(kortlek.pop()) # och samtidigt ta bort det kortet från listan och då passar pop() bra då den tar det sista värdet och 
    spelareHand.append(kortlek.pop()) # lägger in det i den nya listan istället. Vi gör detta två gånger så spelare får två kort.



    # Nu ska vi göra själva loopen för att låta spelaren ta fram lite kort
    while True:
        # Spelaren ska först få två kort i handen:
        spelareSumma = int(sum(spelareHand)) # För att spelaren ska veta sin totala poäng behöver vi veta den totala summan som kortena är värda, det gör vi med funktionen sum som summerar alla värden i en lista
        # Vi vill nu printa vad spelaren fick:
        print(f"Du fick korten: {spelareHand}, poäng: {spelareSumma}")
        # En if-sats som kollar om spelarens summa gick över 21 och därmed förlorat
        if spelareSumma > 21: 
            print (f"Din hand är värd {spelareSumma} och överskred 21, tyvärr så har du förlorat!")
            break
        # Else if-sats som kollar om spelarens summa är exakt 21 och därmed inte behöver dra mer kort.
        elif spelareSumma == 21:
            print("Blackjack! Du har 21 poäng nu!")

        # Om värdet är under 21 så får man frågan om man vill dra ett till kort
        tillKort = input("Vill du dra ett till kort (ja/nej) > ").lower() # .lower() i slutet så oavsett hur användaren skriver ja (tex Ja, JA, jA) så sparar vi det med lowercase för att matcha vår if-sats
        # Nu kollar vi med en if-sats ifall spelaren vill ha ett nytt kort eller inte
        if tillKort == "ja": # Svar ja
            nyttKort = kortlek.pop() # Ny variable för att lägga till kort så vi kan skriva ut vilket kort spelaren fick
            spelareHand.append(nyttKort) # 
            print(f"Du fick kort {nyttKort}!")
        elif tillKort == "nej": # Svar nej
            break
        else: # SKrivit fel svar
            print("Du behöver ange antingen ja eller nej > ")

    # Denna loop gör så datorn drar ett kort sålänge den har en totalsumma under 17
    while sum(datorHand) < 17:
        datorHand.append(kortlek.pop()) # Lägger in ett kort till den tomma listan vi gjorde tidigare kallad datorHand
    datorSumma = int(sum(datorHand)) # Räknar ut datorns totala summa
    print(f"Datorns kort är: {datorHand}, poäng: {datorSumma}") # Skriver ut vad datorn fick

    if spelareSumma > 21: # Om spelare gick över summan 21 så har den förlorat
        print(f"Du gick över 21 (du fick {spelareSumma}) och därmer vinner datorn!")
    elif datorSumma > 21 or spelareSumma > datorSumma: # Om datorn gick över 21 eller om spelaren hade högre värde än datorn så vinner spelaren
        print(f"Grattis du fick {spelareSumma} medans datorn fick {datorSumma}, du vann!")
    elif spelareSumma == datorSumma: # Om spelaren har exakt samma värde som datorn blir det oavgjort
        print(f"Oavgjort, ni båda fick {spelareSumma}")
    else: # Om datorn fick ett högre värde än spelaren förlorar man 
        print(f"Du fick {spelareSumma} och datorn fick {datorSumma}, tyvärr har du förlorat dina pengar.")