Deze bestanden zijn gebruikt om data schoon te maken en om aanpassingen te maken. Hieronder een lijst van wat elk bestand doet.

addUnixTime.py: Voegt naast timestamp ook de unix tijd toe aan reading.\
calculatinRawValues.py: van normale waardes weer ruwe waardes maken aan de hand van kalibratie profiel\
changingLatLong.py: Lat long aanpassing van lezing omdat dit soms fout kan gaan.\
getRawReadings.py: Haal de Ruwe waardes op uit de SQL database.\
makeCSV.py: Vanuit de SQL DB een csv coor azure gebruik.\
makingGraph.py: Maak grafiek bodemvochtigheid van sensoren over alle meetingen die ze hebben gedaan.\
pastRain.py: Vergelijking met regen en verschillende waardes om te kijken voor correlatie.\
soilMoistureClean.py: Haal slechte bodemvochtigheid waardes uit Mongo DB.\
testRegenNU.py: Zelfde als pastRain maar dan kijken naar de toekomst.\
transportingData.py: Vanuit SQL database maak csv van Azure op basis van goeie sensore en haal hierbij weer data op.\
weatherApi.py: Krijg data over het weer vanuit api.
