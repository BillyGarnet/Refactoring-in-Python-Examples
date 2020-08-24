# Extract constant to improve readability
MIN_QUANTITY = 0
MAX_QUANTITY = 50

def ExtractConstant(self, item):

    if item.name == "Apple":
        if item.quantity > MIN_QUANTITY:
            item.quantity = item.quantity - 1
    else:
        if not item.quantity < MAX_QUANTITY:
            item.quantity = item.quantity + 1

