import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Bruker pandas for å lese inn data fra CSV-fil
def load_data():
    data = pd.read_csv('spi_global_rankings.csv')
    return data

# Del 1: brukeren velger fotballiga
def choose_league(data):
    leagues = data['league'].unique()

    # Fjern alle UEFA-ligaer (Champions League, Europa League, ...)
    for league in leagues:
        if "UEFA" in league:
            leagues = np.delete(leagues, np.where(leagues == league))
    
    # Vis alternativer i terminalen
    print("Velg en fotballiga:")
    for i, league in enumerate(leagues):
        print(f"{i+1}. {league}")
    
    # Få brukeren til å velge liga, og lagre valgt data
    # Sjekk for gyldig input
    while True:
        try:
            league_choice = int(input("Skriv inn tallet på ligaen du ønsker, og trykk [ENTER]: ")) - 1
            if league_choice < 0 or league_choice >= len(leagues):
                raise IndexError
            selected_league = leagues[league_choice]
            return selected_league
        except (ValueError, IndexError):
            print("Ugyldig input. Vennligst skriv inn et gyldig tall.")

# Del 2: brukeren velger to fotballklubber å sammenlikne
def choose_clubs(data, selected_league):
    # Filtrer basert på den valgte ligaen
    league_data = data[data['league'] == selected_league]
    clubs = league_data['name'].unique()
    
    # Vis alternativer i terminalen
    print(f"\nVelg to fotballklubber fra {selected_league}:")
    for i, club in enumerate(clubs):
        print(f"{i+1}. {club}")

    selected_clubs = []
    
    # Få brukeren til å velge første klubb
    while True:
        try:
            club_choice_1 = int(input("Skriv inn nummeret på den første fotballklubben, og trykk [ENTER]: ")) - 1
            if club_choice_1 < 0 or club_choice_1 >= len(clubs):
                raise IndexError
            selected_clubs.append(clubs[club_choice_1])
            break
        except (ValueError, IndexError):
            print("Ugyldig input. Vennligst skriv inn et gyldig tall.")
    
    # Få brukeren til å velge andre klubb
    while True:
        try:
            club_choice_2 = int(input("Skriv inn nummeret på den andre fotballklubben, og trykk [ENTER]: ")) - 1
            if club_choice_2 < 0 or club_choice_2 >= len(clubs):
                raise IndexError
            
            # sjekk at samme klubb ikke velges to ganger
            if club_choice_2 == club_choice_1:
                raise ValueError
            selected_clubs.append(clubs[club_choice_2])
            break
        except (ValueError, IndexError):
            print("Ugyldig input. Vennligst skriv inn et gyldig tall.")
    
    return selected_clubs
    
# Del 3: sammenlikne to fotballklubber og visualisere resultatet
def compare_clubs(data, selected_league, selected_clubs):
    # Filtering basert på valgt liga og klubb
    club_data = data[(data['league'] == selected_league) & (data['name'].isin(selected_clubs))]

    indices = club_data.index
    num_attributes = 2
    bar_width = 0.35 # størrelse på søyler
    positions = range(1, num_attributes + 1)
    attributes = ['offense', 'defense']
    colors = ['thistle', 'mediumpurple']
    # farger hentet fra: https://matplotlib.org/stable/gallery/color/named_colors.html

    # lag et søylediagram (gruppert, slik at det er enklere å sammenlikne)
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, idx in enumerate(indices):
        values = club_data.iloc[i, 4:6]  # offense og defense er kolonne 4 og 5
        ax.bar([p + i * bar_width for p in positions], values, bar_width, label=club_data.iloc[i]['name'], color=colors[i])

    # legg på labels og tittel
    ax.set_ylabel('Ranking')
    ax.set_title(f'Comparison of {selected_clubs[0]} and {selected_clubs[1]} in {selected_league}')
    ax.set_xticks([p + bar_width / 2 for p in positions])
    ax.set_xticklabels(attributes)
    ax.legend()
    plt.show()

def main():
    # last inn datafil, hent liga, helt klubbene, sammenlikn og visualiser
    data = load_data()
    selected_league = choose_league(data)
    selected_clubs = choose_clubs(data, selected_league)
    compare_clubs(data, selected_league, selected_clubs)

# kjør programmet :)
if __name__ == "__main__":
    main()
