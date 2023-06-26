import csv
import matplotlib.pyplot as plt

# målinger hver time, fra time 0 til 23

data = "meter.csv"

# beregn gjennomsnittlig forbruk per time
def calculate_average_power(filename):
    average = [0] * 24
    hours = [0] * 24 

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) # hopp over header

        for row in reader:
            # definer hvilke kolonne som skal leses:
            # 0 = dato, 1 = time, 2 = forbruk
            hour = int(row[1])
            power = float(row[2])

            average[hour] += power # oppdater totalt forbruk per time
            hours[hour] += 1 # tell antall målinger per time

    # beregn gjennomsnittsverdi for hver time (24)
    for i in range(24):
        if hours[i] > 0:
            average[i] /= hours[i]

    return average

# beregn minimumsverdi per time
def calculate_minimum_power(filename):
    # starter med 1000, så vil alle målinger være mindre
    min_value = [1000] * 24

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            hour = int(row[1])
            power = float(row[2])

            # oppdater minimumsverdi
            if power < min_value[hour]:
                min_value[hour] = power

    return min_value

# beregn maksimumsverdi per time
# samme konsept som minimun, men oppdaterigen er motsatt
def calculate_maximum_power(filename):
    # starter med 0, så vil alle målinger være større
    max_value = [0] * 24

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) 

        for row in reader:
            hour = int(row[1])
            power = float(row[2])

            if power > max_value[hour]:
                max_value[hour] = power

    return max_value

# kjør funksjonene og lagre resultatene i variabler
# dette er lister med 24 elementer (en per time)
averages = calculate_average_power(data)
minimums = calculate_minimum_power(data)
maximums = calculate_maximum_power(data)

# farger for linjene
color = ['mediumseagreen', 'slateblue', 'hotpink'] # ref: https://matplotlib.org/stable/gallery/color/named_colors.html

# plott tre ganger
plt.plot(maximums, label="Maksimalt forbruk per time", color=color[0])
plt.plot(averages, label="Gjennomsnittlig forbruk per time", color=color[1])
plt.plot(minimums, label="Minimum forbruk per time", color=color[2])

# beskrivelser og tittel
plt.xlabel("Time på døgnet (0-23)")
plt.ylabel("Forbruk i kWh")
plt.title("Forbruk per time i løpet av en måned")
plt.legend()

# lagre som bilde (png)
plt.savefig("power.png")
