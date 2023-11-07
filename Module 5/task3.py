def sanitize_phone_number(phone):
    remove_probel = phone.strip ()
    remove_char = remove_probel.replace("(", "").replace("-", "").replace(")", "").replace("+", "").replace(" ", "")
    return remove_char

    


a = "38050 111 22 11"
    # "     0503451234",
    # "(050)8889900",
    # "38050-111-22-22",
    # "38050 111 22 11   ", 
b = sanitize_phone_number (a)
print (b)