
def extract_method(first_throw, person):
    my_string = ""

    if first_throw > 5:
        my_string = "Good start!"
        term = "Major"
    else:
        my_string = "Bad start."
        term = "Minor"
    my_string = max_20_chars(my_string, term)
    person.score += first_throw

    my_string += term

    # extract constant then method to improve complicated if statement
    is_impressive = impressive(first_throw, term)
    if is_impressive:
        my_string += " Impressive!"

    return my_string


def impressive(first_throw, term):
    return len(term) > 5 and "Major" in term and first_throw < 10


def max_20_chars(my_string, term):
    my_string += term
    if len(my_string) > 20:
        my_string = my_string[:20]
    return my_string
