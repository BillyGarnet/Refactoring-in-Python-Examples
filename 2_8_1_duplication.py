# Duplication
# Duplication

def duplication_example(self, food, groceries_list):
    my_string = ""

    if food.name == "Apple":
        groceries_list.append("Apple")
        favorite_snack = "Apple"

    elif food.name == "Coconut":
        groceries_list.append("Coconut")
        favorite_snack = "Coconut"

    elif food.name == "Orange":
        groceries_list.append("Orange")
        favorite_snack = "Orange"

    for item in groceries_list:
        if item in ["Apple", "Orange", "Coconut"]:
            vitamins = vitamins + " C"
        if item == "Coconut":
            vitamins = vitamins + " E B1 B3 B5 B6"

    my_string = my_string + favorite_snack + vitamins
    return my_string