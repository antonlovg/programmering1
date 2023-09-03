# Spelet Tjugoett gjord av Anton Lövgren
# Syftet med spelet är att komma närmst 21 men inte över, spelaren med högst valör i handen vinner alternativt lika om man har samma valörer oavsett vilka kort man har.
# Knekt, dam och kung räknas som 10. Ess räknas som 1 eller 14

import random # Importar modulen som heter random (tidigare använt i lektion 3) som gör att vi kan ta fram slumpmässiga kort.

# Kortleken
kort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Detta är alla värden som vi har i en kortlek. Vi vill att 1 (ess) ska kunna bli 14 men ENDAST om man inte går över 21 och detta kollar vi med en if-sats.
kortlek = kort * 4 # Detta gör vi eftersom varje valör finns med fyra exemplar dvs 52 kort totalt.
random.shuffle(kortlek) # Precis som vi skulle blanda korten för hand så gör vi detta med shuffle, nu ligger listan i en slumpmässig ordning med fyra st exemplar av varje valör