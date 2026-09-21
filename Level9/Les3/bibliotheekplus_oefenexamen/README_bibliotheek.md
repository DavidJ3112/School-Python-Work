# BibliotheekPlus - Uitleenregistratie Systeem

## Oefenexamen Python MBO-4

### Doel
Analyseer uitleengegevens van een bibliotheek om inzicht te krijgen in leengedrag en te laat ingeleverde boeken.

### Bestanden

- `bibliotheek_uitleningen.py` - Studentenversie met opdrachten (te voltooien)
- `bibliotheek_uitleningen_compleet.py` - Nakijkmodel (voor docent)
- `Boekencatalogus.csv` - Lijst met alle boeken in de catalogus
- `Uitleningen/` - Map met CSV bestanden per boek met uitleengegevens (LET OP: in de code staat "Temp/" - dit moet je aanpassen!)
- `Procesbeschrijvingen_Bibliotheek.docx` - Procesbeschrijvingen om in te vullen
- `Procesbeschrijvingen_Bibliotheek_ANTWOORDEN.docx` - Antwoordmodel procesbeschrijvingen

### Bestandsformaten

#### Boekencatalogus.csv
```
BOEKNUMMER_DATUM,Titel
B1234_15012026,De Ontdekking van de Hemel
B2468_15012026,Het Diner
```

#### Uitleningen directory
Bestandsnaam format: `BOEKNUMMER_DATUM_MAXUITLEENDAGEN.csv`

Voorbeeld: `B1234_15012026_21.csv`
- B1234 = Boeknummer (cadeau! Dit staat in de bestandsnaam)
- 15012026 = Datum (DDMMYYYY)
- 21 = Maximaal aantal uitleendagen

Inhoud CSV:
```
Jan Jansen,14
Piet Pietersen,7
Marie de Vries,21
```
Kolom 0 = Naam lener, Kolom 1 = Aantal dagen uitgeleend

### Opdrachten

Zoek in de code naar `#***` om de opdrachten te vinden. Je moet:

1. **Voorbereiding**
   - Pas het pad naar het boekencatalogus bestand aan
   - Pas het pad naar de uitleningen directory aan
   - Vraag de gebruiker om een datum
   - Print de huidige datum en tijd

2. **Data verwerken per boek**
   - Haal de boek_datum en max_dagen uit de bestandsnaam
   - Check of de datum klopt
   - Bereken totaal aantal uitleendagen per boek
   - Tel aantal uitleningen per boek
   - Check hoeveel uitleningen te laat zijn (dagen > max_dagen)
   - Bereken gemiddelde uitleenduur
   - Bewaar gegevens in dictionary
   - Print statistieken per boek

3. **Totalen berekenen**
   - Bereken totaal dagen van alle boeken
   - Bereken totaal aantal uitleningen
   - Print de totalen

4. **Niet uitgeleende boeken**
   - Vind boeken die in de catalogus staan maar geen uitleningen hebben

### Test

Voer datum in: `15012026`

Verwachte output (ongeveer):
```
21:30 30-01-2026
==================================================
BibliotheekPlus - Uitleenregistratie Systeem
==================================================
Boek B1234: 7 uitleningen | Totaal: 107 dagen | Gem: 15.3 dagen | Te laat: 1
Boek B2468: 5 uitleningen | Totaal: 75 dagen | Gem: 15.0 dagen | Te laat: 2
Boek B3579: 4 uitleningen | Totaal: 52 dagen | Gem: 13.0 dagen | Te laat: 0
Boek B4680: 5 uitleningen | Totaal: 27 dagen | Gem: 5.4 dagen | Te laat: 1

Totaal dagen uitgeleend: 261
Totaal aantal uitleningen: 21
Bestand:  Niet_Uitgeleend_15012026.csv  aangemaakt
```

### Tips
- Begin met het aanpassen van de paden en het testen of bestanden ingelezen worden
- Gebruik print statements om te debuggen
- Let op de indentatie in Python!
- Kijk naar het voorbeeld format van de bestanden
