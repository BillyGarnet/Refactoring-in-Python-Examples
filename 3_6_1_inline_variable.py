# inline and extract working together
def inline_variable(first_throw, person):
    my_string = ""
    start = ""

    if first_throw > 5:
        my_string = max_20("Good start!", "Major")
    else:
        my_string = max_20("Bad start.", "Minor")

    person.score += first_throw

    # extract constant then method to improve complicated if statement
    if impressive(first_throw, my_string):
        my_string += " Impressive!"

    return my_string


def impressive(first_throw, my_string):
    return len(my_string) > 5 and "Major" in my_string and first_throw < 10


def max_20(my_string, term):
    my_string += term
    # make sure string has less then 20 chars
    if len(my_string) > 20:
        my_string = my_string[:20]
    return my_string
