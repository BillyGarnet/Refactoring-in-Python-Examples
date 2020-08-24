def fizzbuzz(number):

    substitute = [(3, "Fizz"), (5, "Buzz")]
    return [''.join(s for d, s in substitute if x % d == 0) or str(x)
            for x in range(1, number+1)]