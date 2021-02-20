def get_unique_ingredients(list_of_pizzas):
    ingredients = []
    for pizza in list_of_pizzas:
        ingredients += pizza
    return set(ingredients)
