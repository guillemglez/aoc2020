from typing import List, Dict

with open('input') as f:
    inpt = f.read().strip()

all_ingredients: List[str] = []
allergic_foods: Dict[str, List[List[str]]] = {}
for line in inpt.split('\n'):
    ingredients = line.split('(contains')[0].split()
    all_ingredients += ingredients
    contains = line.strip()[:-1].split('(contains ')[1].split(', ')
    for allergen in contains:
        if allergen not in allergic_foods:
            allergic_foods[allergen] = []
        allergic_foods[allergen].append(ingredients)

allergens: Dict[str, List[str]] = {}
for allergen, recipes in allergic_foods.items():
    susceptible = list(
        set([ingredient for recipe in recipes for ingredient in recipe]))
    for ingredient in susceptible:
        if ingredient not in allergens:
            allergens[ingredient] = []
        for recipe in recipes:
            if ingredient not in recipe:
                break
        if ingredient in recipe:
            allergens[ingredient].append(allergen)

count = 0
for ingredient, susceptible in allergens.items():
    if len(susceptible) == 0:
        count += all_ingredients.count(ingredient)

print(
    f"Confidently non-allergic ingredients appear {count} times in the list.")
