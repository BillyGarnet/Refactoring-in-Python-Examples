def comment_code(first_ball, second_ball):
    # comment used as section label

    my_result = 1 + first_ball

    # calculate total
    total = sum(second_ball for i in range(5) if i % 2 == 0)
    my_result = my_result + total

    return my_result
