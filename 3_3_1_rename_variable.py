# What is value? A better name would tell us what this is doing
def calculate_total(first_throw):
    total = 0
    for _ in range(5):
        total = total + first_throw
    return total
