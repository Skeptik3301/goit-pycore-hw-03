def get_numbers_ticket(min, max, quantity):
    import random 
    lottery_numbers = random.sample(range(min>=1, max+1), quantity)
    return lottery_numbers
lottery_numbers = get_numbers_ticket(1, 10, 3)
print("6,9,2", lottery_numbers)

   
