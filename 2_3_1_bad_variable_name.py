def bad_variable_name(self, x, region):

    # bad variable name
    data = {1 , 2, 3}
    cty_nmb = 0
    cty_nmb2 = 42
    cty_strng = "Spam"
    if x == 7:
        cty_nmb = 1
        cty_strng = "Ottawa"
    elif x == 5:
        cty_nmb = 2
        cty_strng = "Canada"
    else:
        cty_nmb = 3
        cty_strng = "Outside Canada"

    # good variable name
    region_codes = {1 , 2, 3}
    area_code = 0
    country_ = 42
    city = "Spam"
    area = ""
    if region == 7:
        area_code = 1
        area = "Ottawa"
    elif region == 5:
        area_code = 2
        area = "Canada"
    else:
        area_code = 3
        area = "Outside Canada"


