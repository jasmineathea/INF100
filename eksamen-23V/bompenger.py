from datetime import datetime, time, timedelta

# input-data:
kryss = [
    ('EZ12345', '2023-04-12T08:10'),
    ('AB23445', '2023-04-12T12:30'),
    ('EY11115', '2023-04-12T10:21'),
    ('ABC-123', '2023-04-12T09:10'),
    ('UB43212', '2023-04-12T05:10'),
    ('EY11115', '2023-04-13T15:21'),
    ('EY11115', '2023-04-13T15:23'),
    ('EY11115', '2023-04-13T15:26'),
    ('EY11115', '2023-04-13T15:28'),
    ('EY11115', '2023-04-13T17:29'),
    ('AB23445', '2023-04-14T12:45'), 
    ('ABC-123', '2023-04-16T12:10'),   
]

# hent timestamp fra kryss-datatypen:
tp = []
for k in kryss:
    tp.append(datetime.fromisoformat(k[1]))

## Tillegg A: rushtid
def rushtime(tp):
    early_rush = False
    late_rush = False

    # tp er en liste med datetime-objekter (2023, 4, 12, 8, 10 for første element)
    # vi må hente ut tidspunktet (8, 10) fra datetime-objektet
    for dt in tp:
        if (dt.time() >= time(6, 30)) and (dt.time() <= time(9, 0)):
            early_rush = True
        if (dt.time() >= time(14, 30)) and (dt.time() <= time(16, 30)):
            late_rush = True

    return early_rush or late_rush

## Tillegg B: gjentatte krysninger
def repeated_crossings(tp):
    repeated = False

    for i in range(len(tp)-1):
        # sjekk om det er mindre enn 60 minutter mellom to kryssninger (i og i+1)
        if (tp[i+1] - tp[i]) < timedelta(minutes=60):
            repeated = True

    return repeated


### Basis:
# tillegg er lagt inn her for å unngå å skrive samme kode flere ganger

def calculate_month(kryss):
    total_sum = {} # dicts for riktig formatering i output
    crossing = {}
    
    for k in kryss:
        vehicle = k[0]
    
        # beregn pris for hver biltype
        if vehicle[0] == 'E':
            # tillegg A: sjekk rushtid
            if rushtime(tp):
                price_per_crossing = 17.60
            else:
                price_per_crossing = 9.60
        else:
            if rushtime(tp):
                price_per_crossing = 46.40
            else:
                price_per_crossing = 22.40
        
        # tell antall krysnigner
        if vehicle in crossing:
            # tillegg B: sjekk tid mellom kryssninger
            if repeated_crossings(tp):
                crossing[vehicle] += 1
        else:
            crossing[vehicle] = 1

        # tillegg C: månedstak
        # etter 60 krysninger er det gratis
        if crossing[vehicle] > 60:
            price_per_crossing = 0
        
        total_sum[vehicle] = price_per_crossing * crossing[vehicle]

        # uten formetering ser output slik ut (basis):
        # {'EZ12345': 9.6, 'AB23445': 44.8, 'EY11115': 57.599999999999994, 'ABC-123': 44.8, 'UB43212': 22.4}
        # formaterer slik at det blir 1 desimal i output
        for vehicle, total in total_sum.items():
            total_sum[vehicle] = round(total, 1) # ref. https://www.programiz.com/python-programming/methods/built-in/round

    return total_sum

# test
print(calculate_month(kryss))

## output: 
{'EZ12345': 17.6, 'AB23445': 92.8, 'EY11115': 105.6, 'ABC-123': 92.8, 'UB43212': 46.4}
