# Negative Logic

def NegativeExample(garbage, item):

    if item.name != "Apple":
        if item.name != "Pear":
            if item.quantity > 0:
                if item.name != "Orange":
                    item.quantity = item.quantity - 1
        else:
            item.quantity = item.quantity - item.quantity
    else:
        if not item.quantity >= 50:
            item.quantity = item.quantity + 1
