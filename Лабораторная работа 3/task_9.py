salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

spend_ = increase + 1
budget = salary - spend
for i in range(1, months + 1):
    i = spend - salary
    spend = spend * spend_
    need_money += i

print(round(need_money))
