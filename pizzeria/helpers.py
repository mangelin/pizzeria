def get_unique_ingredients(listOfPizzas, pizzas):
    ingredients = []
    for pizza_id in listOfPizzas:
        ingredients += pizzas[pizza_id]
    return set(sorted(ingredients))