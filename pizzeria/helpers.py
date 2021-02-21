def get_unique_ingredients(listOfPizzas, pizzas):
    ingredients = []
    for pizza_id in listOfPizzas:
        ingredients += pizzas[pizza_id]
    return set(sorted(ingredients))


def calculate_score(pizzas_to_deliver, pizzas_menu):
    score = 0
    for pizza_ids in pizzas_to_deliver:
        score += len(get_unique_ingredients(pizza_ids, pizzas_menu)) ** 2
    return score

