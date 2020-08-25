# Commented out zombie code

def update_my_string(my_string, increment, value1, term):
    for _ in range(value1):
        while value1 >= increment:
            my_string += term
            value1 -= increment
    return my_string


def duplication_example(primary_value):
    my_string = ""

    increment = 10
    for _ in range(primary_value):
        while primary_value >= increment:
            my_string += "Major"
            primary_value -= increment

    another_increment = 50
    term = "Another"
    my_string = update_my_string(my_string, another_increment, primary_value, term)


    return my_string
