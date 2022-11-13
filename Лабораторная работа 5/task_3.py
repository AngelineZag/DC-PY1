from random import randint

def get_unique_list_numbers() -> list[int]:
    random_numbers = [randint(-10, 11) for _ in range(15)]
    unique_numbers = "".join([str(digit) for digit in random_numbers])
    return [unique_numbers]

unique_numbers = get_unique_list_numbers()
print(unique_numbers)
print(len(unique_numbers) == len(set(unique_numbers)))

