""" Zorg ervoor dat je code goed is opgeslagen in de daarvoor bestemde folder of locatie."""
""" Opdrachten zijn voorzien van #*** """
""" QuickWings Luchthaven - Ticket Analyse Systeem """
import os

#leest uit een bestand de data en slaat dit op in een array
def lees_bestand(bestandsnaam):
    data = []  
    with open(bestandsnaam, 'r') as bestand:
        for regel in bestand:
            rij = regel.strip().split(',')  
            data.append(rij)
    return data

def vind_ontbrekende():        
    #maakt een array met ontbrekende vluchten
    ontbrekende_vluchten = []
    for vlucht in vluchtcodes:
            #*** check of vlucht datum klopt met zoek_datum
            #*** check of de vluchtcode voorkomt in vlucht_gegevens (als deze niet voorkomt, voer de volgende regel uit)
            ontbrekende_vluchten.append(vlucht)

    bestand_ontbrekende_vluchten = f'Ontbrekende_Vluchten_{zoek_datum}.csv'
    # schrijft de ontbrekende vluchten naar csv    
    with open(bestand_ontbrekende_vluchten, 'w') as bestand:
        for code in ontbrekende_vluchten:
            bestand.write(str(code) + ',\n')
        print("Bestand: ", bestand_ontbrekende_vluchten, " aangemaakt")   

def lees_alle_vluchten():
    totaal_omzet = 0
    totaal_passagiers = 0

    #gaat langs alle bestanden in de directory
    for bestandsnaam in os.listdir(directory):
        f = os.path.join(directory, bestandsnaam) #haalt het hele path voor dat bestand op
        #checkt of f een bestand is
        if os.path.isfile(f):
            # Bestandsnaam format: VLUCHTCODE_DATUM_MAXPASSAGIERS.csv
            # Voorbeeld: KL1234_15012026_180.csv
            delen = bestandsnaam.replace('.csv', '').split('_')
            vluchtcode = delen[0]
            #*** haal uit delen de vlucht_datum en max_passagiers
            
            
            #*** check of vlucht datum klopt met zoek_datum
            
                bestanddata = lees_bestand(f)
                
                vlucht_omzet = 0
                aantal_verkocht = 0
                for waarde in bestanddata:
                    ticketprijs = float(waarde[1]) #prijs staat in kolom 1
                    #*** bereken totaal omzet van deze vlucht
                    #*** tel aantal verkochte tickets (elke regel is 1 ticket)
                
                #*** bereken gemiddelde ticketprijs voor deze vlucht
                
                #*** bewaar in vlucht_gegevens de vluchtcode + omzet gegevens
                #*** print vluchtcode, verkocht/max, totaal omzet, gemiddelde prijs
                
        #*** bereken totaal omzet alle vluchten deze datum
        #*** bereken totaal aantal verkochte tickets
            
    #*** print totaal omzet 
    #*** print totaal aantal passagiers

#*** pas path aan naar vluchtcodes bestand
vlucht_bestand = "Temp"
vluchtcodes = lees_bestand(vlucht_bestand)
vlucht_gegevens = dict()

#*** print de datum en tijd in format UU:MM DD-MM-YYYY

directory = "Temp/" #*** pas path aan naar folder met de csv vlucht bestanden
zoek_datum = "15012026" #*** vraag gebruiker om een datum in format DDMMYYYY

lees_alle_vluchten()
vind_ontbrekende()

input("druk op een willekeurige toets om applicatie te sluiten")
