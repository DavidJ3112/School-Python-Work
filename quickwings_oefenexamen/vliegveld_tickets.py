""" Zorg ervoor dat je code goed is opgeslagen in de daarvoor bestemde folder of locatie."""
""" Opdrachten zijn voorzien van #*** """
""" QuickWings Luchthaven - Ticket Analyse Systeem """
import os
from datetime import datetime
from ANSI import ANSI

Debug = True

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
            datum = delen[1]
            formated_datum = datetime.strptime(datum, "%d%m%Y")
            max_passagiers = delen[2]

            if Debug == True: print(delen)
            print(f"{ANSI.BLUE}{ANSI.SAPERATOR}{ANSI.RESET}")
            print(f"{ANSI.MAGENTA}Flight Code: {vluchtcode}{ANSI.RESET}")
            print(f"{ANSI.MAGENTA}Date: {formated_datum:%d-%m-%Y}{ANSI.RESET}")
            print(f"{ANSI.MAGENTA}Max_Passagiers: {max_passagiers}{ANSI.RESET}")
            
            #*** check of vlucht datum klopt met zoek_datum
            if datum == zoek_datum:
                if Debug == True: print(F"{ANSI.GREEN}Success{ANSI.RESET}")
            
                bestanddata = lees_bestand(f)
                if Debug == True: print(bestanddata)
                
                vlucht_omzet = 0
                aantal_verkocht = 0
                for waarde in bestanddata:
                    ticketprijs = float(waarde[1]) #prijs staat in kolom 1
                    vlucht_omzet += ticketprijs
                    aantal_verkocht += 1
                    if Debug == True: print(f"{ANSI.MAGENTA}{ticketprijs = }, {vlucht_omzet = }, {aantal_verkocht = }{ANSI.RESET}")
                    #*** bereken totaal omzet van deze vlucht
                    #*** tel aantal verkochte tickets (elke regel is 1 ticket)
                
                #*** bereken gemiddelde ticketprijs voor deze vlucht
                Average_Price: float = vlucht_omzet / aantal_verkocht
            

                #*** bewaar in vlucht_gegevens de vluchtcode + omzet gegevens
                vlucht_gegevens[vluchtcode] = {
                    "verkocht": aantal_verkocht,
                    "omzet": vlucht_omzet,
                    "gemiddelde": Average_Price
                }
                #*** print vluchtcode, verkocht/max, totaal omzet, gemiddelde prijs
                print(ANSI.MAGENTA,
                    f"vlucht {vluchtcode} | "
                    f"verkocht: {aantal_verkocht}/{max_passagiers} | "
                    f"omzet: €{vlucht_omzet:.2f} | "
                    f"gemiddelde prijs: €{Average_Price:.2f}"
                    ,ANSI.RESET
                )
                
            else:
                if Debug == True: print(F"{ANSI.RED}Failed{ANSI.RESET}")
                return

                
        print(vlucht_gegevens)

        #*** bereken totaal omzet alle vluchten deze datum
        #*** bereken totaal aantal verkochte tickets
            
    #*** print totaal omzet 
    #*** print totaal aantal passagiers



#*** pas path aan naar vluchtcodes bestand
vlucht_bestand = r"C:\Git_repos\School-Python-Work\quickwings_oefenexamen\Vluchtcodes_v2.csv"
vluchtcodes = lees_bestand(vlucht_bestand)
vlucht_gegevens = dict()

#*** print de datum en tijd in format UU:MM DD-MM-YYYY

nu = datetime.now()
print(f"{ANSI.MAGENTA}{nu.strftime("%H:%M %d-%m-%Y")} {ANSI.RESET}")

directory = r"C:\Git_repos\School-Python-Work\quickwings_oefenexamen\Vluchten" #!# #*** pas path aan naar folder met de csv vlucht bestanden
# zoek_datum = "15012026" #!# #*** vraag gebruiker om een datum in format DDMMYYYY
if Debug == True:
    zoek_datum = "15012026"
else:
    zoek_datum = input(f"{ANSI.CYAN}vull de datum in formatage DDMMYYYY {ANSI.RESET}")

lees_alle_vluchten()
vind_ontbrekende()

input("druk op een willekeurige toets om applicatie te sluiten")
