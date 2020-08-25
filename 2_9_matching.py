# Matching Code

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


    return my_string
