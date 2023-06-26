Lab 13 INF100, vår 2023
av Jasmine Næss
------------------------------------

---- Om programmet:
Datasettet spi_global_rankings.csv er hentet fra FourTwentyThree sine datasett under kategorien Soccer predictions.
Her finner vi nylig oppdatert data med rangering av ulike fotballklubber fra hele verden (altså, ingen landslag).
Jeg bruker spesifikt tallene fra 'off' (offense) og 'def' (defense).

---- Endringer underveis:
Om man tar med alle ligaene fra datasettet, ser lista slik ut:

1. Barclays Premier League
2. German Bundesliga
3. Spanish Primera Division
4. Italy Serie A
5. Portuguese Liga
6. French Ligue 1
7. Russian Premier Liga
8. Scottish Premiership
9. Dutch Eredivisie
10. Austrian T-Mobile Bundesliga
11. Brasileiro Série A
12. Swiss Raiffeisen Super League
13. Mexican Primera Division Torneo Clausura
14. Turkish Turkcell Super Lig
15. Belgian Jupiler League
16. UEFA Europa Conference League
17. UEFA Champions League
18. English League Championship
19. Greek Super League
20. Norwegian Tippeligaen
21. Argentina Primera Division
22. UEFA Europa League
23. Danish SAS-Ligaen
24. Major League Soccer
25. Japanese J League
26. English League One
27. French Ligue 2
28. Swedish Allsvenskan
29. Italy Serie B
30. German 2. Bundesliga
31. Spanish Segunda Division
32. South African ABSA Premier League
33. Australian A-League
34. Chinese Super League
35. United Soccer League
36. English League Two

En ting jeg da merket meg er at UEFA sine ligaer er med, noe jeg ville fjerne;
dette er egne turneringer med en kombinasjon av lag fra flere ligaer.

Når ting var implementert slik jeg ønsket, la jeg også inn funksjoner som sjekket for riktig input.
