# Unused zombie code



def duplication_example(self, primary_value):
    my_string = ""
    # unused variable
    second_string = ""

    increment = 10
    for _ in range(primary_value):
        while primary_value >= increment:
            my_string += "Major"
            primary_value -= increment

    return my_string
