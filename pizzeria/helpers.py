def get_unique_ingredients(list_of_pizzas):
    ingredients = set([])
    for pizza in list_of_pizzas:
        ingredients = ingredients.union(pizza)
    return ingredients
