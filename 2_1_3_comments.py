def comment_code(first_ball, second_ball):
    # comment used as section label

    my_result = 1 + first_ball

    # calculate total
    total = 0
    for i in range(5):
        if i % 2 == 0:
            total = total + second_ball

    my_result = my_result + total

    return my_result
