def fizzbuzz(number):

    return "1"










    # alternate solutions

    # build string
    # result = ""
    # if number % 3 == 0:
    #     result += "Fizz"
    # if number % 5 == 0:
    #     result += "Buzz"
    # if result == "":
    #     result = str(number)
    # return result

    # build string, variation
    # value = str()
    # if number % 3 == 0:
    #     value += "Fizz"
    # if number % 5 == 0:
    #     value += "Buzz"
    # return value or str(number)

    # simple, multiple returns
    # if number % 3 == 0 and number % 5 == 0:
    #     return "FizzBuzz"
    # if number % 3 == 0:
    #     return "Fizz"
    # if number % 5 == 0:
    #     return "Buzz"
    # return str(number)

#     # simple, multiple returns with helper methods
#     if divisble_by_3(number) and divisible_by_5(number):
#         return "FizzBuzz"
#     if divisble_by_3(number):
#         return "Fizz"
#     if divisible_by_5(number):
#         return "Buzz"
#     return str(number)
#
#
# def divisible_by_5(number):
#     return number % 5 == 0
#
#
# def divisble_by_3(number):
#     return number % 3 == 0


   #  compact
   #  if number % 3 == 0 and number % 5 == 0: return "FizzBuzz"
   #  if number % 3 == 0: return "Fizz"
   #  if number % 5 == 0: return "Buzz"
   #  return str(number)

   # fb_dict = {3: "Fizz", 5: "Buzz"}
    # result = str()
    # for key in fb_dict:
    #     if number % key == 0:
    #         result += fb_dict[key]
    #
    # return result or str(number)


    # substitute = [(3, "Fizz"), (5, "Buzz")]
    # return [''.join(s for d, s in substitute if x % d == 0) or str(x)
    #         for x in range(1, number+1)]


    # fb_dict = {3: "Fizz", 5: "Buzz"}
    # result = str()
    # for key, value in fb_dict.items():
    #     if number % key == 0:
    #         result += value
    #
    # return result or str(number)
