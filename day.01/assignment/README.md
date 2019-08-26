# Assignment

Build a command line scraper that accepts:

* a country code (ISO CODE) and tells me which top 4 countries which received imports and the amount for 2017.
* a parameter all, which will then take a list of countries
* a parameter save, which will then save the contents to a csv file


example:

scraper.exe JPN
\> USA 200B
\> CHN 100B
\> HNK 50B
\> KOR 45B

scraper.exe all
AFG
\> SAU 50B
\> IRN 10B
\> KUW 5B
\> CHN 1B
BOL
\> BRA 20B
...
...

scraper.exe all save
\> saving results to results.csv


suggested url to use:
https://wits.worldbank.org/CountryProfile/en/Country/ARG/Year/2017/TradeFlow/Export/Partner/All/Product/Total




