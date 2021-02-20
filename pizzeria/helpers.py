from .types import PIZZAS

def get_unique_ingredients(listOfPizzas):
    ingredients = []
    for pizza in listOfPizzas:
        ingredients += PIZZAS[pizza]
    return set(sorted(ingredients))