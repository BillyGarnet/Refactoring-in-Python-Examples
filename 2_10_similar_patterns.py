#Be consistent
# different ways of doing the same thing is another type of duplication

def update_my_string(my_string, increment, value1, term):
    for _ in range(value1):
        while value1 >= increment:
            my_string += term
            value1 -= increment
    return my_string


def duplication_example(primary_value):
    my_string = ""

    increment = 10
    for i in range(0, primary_value):
        while primary_value >= increment:
            my_string += "Major"
            primary_value -= increment

    second_increment = 1
    for i in range(primary_value):
        while primary_value >= second_increment:
            my_string += "minor"
            primary_value -= second_increment


    another_increment = 50
    term = "Another"
    my_string = update_my_string(my_string, another_increment, primary_value, term)


    return my_string
