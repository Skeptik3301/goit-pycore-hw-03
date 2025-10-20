def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    clean_number = ""

    for i, ch in enumerate(phone_number):
        if ch.isdigit() or (ch == '+' and i == 0):
            clean_number += ch


    if clean_number.startswith('+'):
        return clean_number

    elif clean_number.startswith('0') or clean_number.startswith('3') or clean_number.isdigit():
        return '+38' + clean_number

    else:
        return None


raw_numbers = [
    "067\t123 4567",          
    "(095) 234-5678\n",       
    "+380 44 123 4567",       
    "501234567",           
    "+1 (202) 555-0147",      
    "   +48 123 456 789",     
    "0503451234",             
    "+49 30 901820",         
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers if normalize_phone(num) is not None]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
