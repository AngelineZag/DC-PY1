list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел

unique_numbers = set(list_)

sum_ = sum(unique_numbers)
Len_ = len(unique_numbers)

print(sum_)
print(Len_)
print(round(sum_ / Len_, 5))

