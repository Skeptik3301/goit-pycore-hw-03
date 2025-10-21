import random

def get_numbers_ticket(min_val, max_val, quantity):
    if (
        not isinstance(min_val, int) or
        not isinstance(max_val, int) or
        not isinstance(quantity, int)
    ):
        return []

    if min_val < 1 or max_val > 1000:
        return []

    if min_val > max_val:
        return []

    if quantity > (max_val - min_val + 1) or quantity < 1:
        return []

    numbers = random.sample(range(min_val, max_val + 1), quantity)
    numbers.sort()
    return numbers
lottery_numbers = get_numbers_ticket(-10, 10, 5)
print("Ваші лотерейні числа:", lottery_numbers)
