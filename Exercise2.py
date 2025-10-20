import random

def get_numbers_ticket(min_val, max_val, quantity):
    if min_val > max_val or quantity > (max_val - min_val + 1) or min_val < 0:
        return []
    lottery_numbers = random.sample(range(min_val, max_val + 1), quantity)
    return lottery_numbers
print(get_numbers_ticket(2, 7, 3))
