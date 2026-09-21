""" Zorg ervoor dat je code goed is opgeslagen in de daarvoor bestemde folder of locatie."""
""" Opdrachten zijn voorzien van #*** """
""" BibliotheekPlus - Uitleenregistratie Systeem """
import os

#leest uit een bestand de data en slaat dit op in een array
def lees_bestand(bestandsnaam):
    data = []  
    with open(bestandsnaam, 'r') as bestand:
        for regel in bestand:
            rij = regel.strip().split(',')  
            data.append(rij)
    return data

def vind_niet_uitgeleend():        
    #maakt een array met boeken die niet uitgeleend zijn
    niet_uitgeleend = []
    for boek in boekencatalogus:
            #*** check of boek datum klopt met zoek_datum
            #*** check of de boekcode voorkomt in boek_gegevens (als deze niet voorkomt, voer de volgende regel uit)
            niet_uitgeleend.append(boek)

    bestand_niet_uitgeleend = f'Niet_Uitgeleend_{zoek_datum}.csv'
    # schrijft de niet uitgeleende boeken naar csv    
    with open(bestand_niet_uitgeleend, 'w') as bestand:
        for code in niet_uitgeleend:
            bestand.write(str(code) + ',\n')
        print("Bestand: ", bestand_niet_uitgeleend, " aangemaakt")   

def lees_alle_uitleningen():
    totaal_dagen = 0
    totaal_uitleningen = 0

    #gaat langs alle bestanden in de directory
    for bestandsnaam in os.listdir(directory):
        f = os.path.join(directory, bestandsnaam) #haalt het hele path voor dat bestand op
        #checkt of f een bestand is
        if os.path.isfile(f):
            # Bestandsnaam format: BOEKNUMMER_DATUM_MAXUITLEENDAGEN.csv
            # Voorbeeld: B1234_15012026_21.csv
            delen = bestandsnaam.replace('.csv', '').split('_')
            boekcode = delen[0]
            #*** haal uit delen de boek_datum en max_dagen
            
            
            #*** check of boek datum klopt met zoek_datum
            
                bestanddata = lees_bestand(f)
                
                boek_dagen = 0
                aantal_uitleningen = 0
                te_laat_count = 0
                for waarde in bestanddata:
                    dagen_uitgeleend = int(waarde[1]) #aantal dagen staat in kolom 1
                    #*** bereken totaal aantal uitleendagen van dit boek
                    #*** tel aantal uitleningen (elke regel is 1 uitlening)
                    #*** check of uitlening te laat is (dagen > max_dagen) en tel op
                
                #*** bereken gemiddelde uitleenduur voor dit boek
                
                #*** bewaar in boek_gegevens de boekcode + uitleengegevens
                #*** print boekcode, aantal uitleningen, totaal dagen, gemiddelde, te laat
                
        #*** bereken totaal dagen alle boeken deze datum
        #*** bereken totaal aantal uitleningen
            
    #*** print totaal dagen 
    #*** print totaal aantal uitleningen

#*** pas path aan naar boekencatalogus bestand
boeken_bestand = "Temp"
boekencatalogus = lees_bestand(boeken_bestand)
boek_gegevens = dict()

#*** print de datum en tijd in format UU:MM DD-MM-YYYY

directory = "Temp/" #*** pas path aan naar folder met de csv uitleenbestanden
zoek_datum = "15012026" #*** vraag gebruiker om een datum in format DDMMYYYY

lees_alle_uitleningen()
vind_niet_uitgeleend()

input("druk op een willekeurige toets om applicatie te sluiten")
