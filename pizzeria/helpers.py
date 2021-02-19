from .types import PIZZAS

def get_unique_ingradients(listOfPizzas):
    ingradients = []
    for pizza in listOfPizzas:
        ingradients += PIZZAS[pizza]
    return set(sorted(ingradients))