# Negative Logic

def NegativeExample(garbage, item):

    if item.name == "Apple":
        if not item.quantity >= 50:
            item.quantity = item.quantity + 1

    elif item.name == "Pear":
        item.quantity = item.quantity - item.quantity
    else:
        if item.quantity > 0 and item.name != "Orange":
            item.quantity = item.quantity - 1
