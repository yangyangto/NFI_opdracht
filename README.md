## DNA Profiling Applicatie - NFI Opdracht

Voor deze opdracht is code aangeleverd die een DNA-profiel vergelijkt met een DNA-spoor (zie map beschrijving_opdracht).

De opdracht bestaat uit de volgende onderdelen:

1. CI/CD Pipeline Configureren
    - Automatische testen
    - Integratietest met tijdsrapportage
2. Applicatie opzetten als een API
De API moet valide input kunnen ontvangen en als output aangeven of de vergelijking tussen spoor en profiel succesvol was.

3. Bonus
    - Een Dockerfile voor de applicatie
    - Codekwaliteitschecks in de CI/CD pipeline

### Uitwerking van de opdracht
**API**

Voor het opzetten van de API is gekozen voor FastAPI. De app is op dit moment simpel opgezet, bij verdere groei van de applicatie zouden de bestanden op een andere manier kunnen worden gestructureerd, voor beter overzicht. Daarnaast zou de applicatie idealiter worden omgezet naar een async app.
Een bulk check endpoint zou ook handig zijn, zodat je in een keer een aantal profielen mee kan geven, waar het spoor mee vergeleken kan worden, maar dat was natuurlijk niet de opdracht :).

**Docker**

Naast een Dockerfile is ook een docker-compose-bestand toegevoegd. Dit is een workflow waarmee ik gewend ben te werken, vooral als er databases in het spel zijn. Het biedt daarnaast het gemak om code lokaal te mappen met de code in de container, zodat wijzigingen direct worden opgepikt en de applicatie automatisch herlaadt.

Run de docker setup met de onderstaande command:

```
docker-compose up -d --build
```

**Test en Perfomance**

De testresultaten, gegenereerd door pytest, kunnen met pytest-html als rapport in de browser worden weergegeven. Dit HTML-bestand kan in GitHub Actions als pipeline-artifact worden gedownload. Om beter inzicht te krijgen in de performance van de code, is een Python code profiler toegevoegd, die ook via de pipeline te downloaden is. 

**Pipeline**

Flake8 is toegevoegd als codekwaliteitscheck. Voorlopig staat de "continue on error" aan. Idealiter worden deze checks als pre-commit hook geïntegreerd, zodat code niet gepusht kan worden zonder aan de gestelde criteria te voldoen.