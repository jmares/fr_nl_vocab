# Woordenlijst Français - Nederlands

## Doel

**Anki** ([link](https://apps.ankiweb.net/)) is een goede methode om wat je al geleerd hebt te herhalen of om je kennis even wat op te frissen, maar ik vind het minder geschikt om nieuwe zaken te leren.

Het doel van dit project is om de gegevens uit een bepaalde **Anki** *deck* te presenteren als een website. De woordenlijst wordt per 25 Franse woorden en hun Nederlands vertaling op een pagina getoond. 

De bedoeling is om zo je Franse woordenschat uit te breiden en eenmaal je alle woorden gestudeerd hebt, dan over te schakelen naar **Anki** om je nieuwe woordenschat te testen en te onderhouden.

Geen idee of dit een goede studiemethode is, maar het lijkt me wel een leuk project. Data uit een **Anki** *deck* inlezen via python en exporteren naar een reeks aan elkaar gelinkte statische HTML-pagina's. Later kan daar eventueel wat JavaScript bij te pas komen of kan ik leren om er een Flask of Django website van te maken.

## Structuur

### Project folder

Deze folder bevat de python-scripts.

### Data

Deze folder bevat de als tekst-bestand geëxporteerde gegevens van de **Anki** *deck* [French-Dutch SELOR 8000 words](https://ankiweb.net/shared/info/1203542828).

Misschien dat ik in de toekomst de gegevens naar een SQLite databank of een JSON-bestand exporteer.

### Templates

Deze folder bevat de template voor de HTML-pagina's.

### WWW

Deze folder bevat de website.

## Versies

### 2022-05-07

- Functionele navbar (aparte template)
- Aantal woordparen per pagina variabel
- Alle pagina's aanmaken: 8000:(aantal woordparen per pagina)

Code is nog *quick and dirty*, maar het gaat vooruit.

### 2022-05-07

- inlezen van gegevens uit tekst bestand
- toevoegen van `try-except` wegens enkele eigenaardigheden in data
- HTML template
- gebaseerd op **Bootstrap 5** (*overkill*?)
- 25 eerste woordparen uit lijst worden op HTML pagina getoond
- NAV-bar werkt nog niet, enkel layout
- gebruik van **Bootstrap Icons** in navbar

### To Do volgende versies

- WWW folder leegmaken voor nieuwe pagina's aangemaakt worden
- Layout
- Code in functies groeperen
- Kan dit voor andere **Anki** decks gebruikt worden?