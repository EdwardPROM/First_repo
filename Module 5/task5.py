def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    v_p = {'UA': [], 'JP': [], 'TW': [], 'SG': []}
    
    for num in list_phones:                         
        sort_num = sanitize_phone_number(num)
        matched = False  # Define matched here

        if sort_num.startswith('81'):
            v_p['JP'].append(sort_num)
            matched = True
        elif sort_num.startswith('65'):
            v_p['SG'].append(sort_num)
            matched = True
        elif sort_num.startswith('886'):
            v_p['TW'].append(sort_num)
            matched = True
        elif sort_num.startswith('380'):
            v_p['UA'].append(sort_num)
            matched = True

        if not matched:
            v_p['UA'].append(sort_num)  # Add to 'UA' if not matched
    
    return v_p