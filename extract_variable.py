def fizzbuzz(number):

    # extract variable example
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz" + "Buzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)