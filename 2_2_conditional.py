def arrowhead_code(i, j, k):
    my_result = 0
    if i > 1:
        i = i + 1
        if j > 5:
            if k < 1:
                my_result = my_result + 1
                if j < i: my_result = my_result * 2
            else:
                my_result = my_result - 1
        elif j > 2:
            my_result = my_result + 3
            my_other_result = 9
        else:
            my_result = my_result + 2
    else:
        my_result = 0

    return my_result
