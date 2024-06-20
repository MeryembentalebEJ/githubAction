def calculate_average(values):
    if not values:
        return 0
    # Bug intentionnel : retour de la somme des valeurs au lieu de la moyenne
    return sum(values)  # BUG: should be return sum(values) / len(values)
