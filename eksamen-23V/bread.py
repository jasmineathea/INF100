# Gyldige kombinasjoner av pålegg lagres i en dict:
valid_combinations = {
    "BrownCheese": ["Jam", "Butter"],
    "Jam": ["Butter", "BrownCheese"],
    "Butter": ["Jam", "BrownCheese", "Caviar", "Egg"],
    "Egg": ["Butter", "Caviar"],
    "Caviar": ["Butter", "Egg"],
    "YellowCheese": ["Ham", "Tomato"],
    "Ham": ["YellowCheese", "Tomato", "Cucumber"],
    "Tomato": ["Ham", "YellowCheese", "Cucumber", "Salad"],
    "Cucumber": ["Ham", "Tomato", "Salad"],
    "Salad": ["Tomato", "Cucumber"]
}

# Ingredienser i følge oppgavetekst:
fridge = ["Tomato", "Ham", "YellowCheese", "Jam", "Cucumber", "Caviar",
                         "Salad", "BrownCheese", "Butter", "Egg"]


# Funksjon for alle gyldige kombinasjoner (av tre) basert på innhold i kjøleskapet
def combinations_of_three(fridge):
    combos = []

    for i in range(len(fridge)):
        for j in range(i + 1, len(fridge)): # Unngå duplikater ved å starte på forskjellige indekser
            for k in range(j + 1, len(fridge)):

                # Ingrediens A, B og C
                ingredient_a = fridge[i]
                ingredient_b = fridge[j] 
                ingredient_c = fridge[k] 

                # sjekke om kombinasjonen er gyldig:
                # A inngår i B og C
                # B inngår i A og C
                # C inngår i A og B
                if ingredient_a in valid_combinations[ingredient_b] and ingredient_a in valid_combinations[ingredient_c] and ingredient_b in valid_combinations[ingredient_a] and ingredient_b in valid_combinations[ingredient_c] and ingredient_c in valid_combinations[ingredient_a] and ingredient_c in valid_combinations[ingredient_b]:
                    combos.append([ingredient_a, ingredient_b, ingredient_c])
    
    # Formater output slik at det er enklere å lese
    for topping in combos:
        print(f"Valid toppings for bread: {topping[0]}, {topping[1]}, {topping[2]}")
    
    return combos

# Kjør funksjonen
combinations_of_three(fridge)
