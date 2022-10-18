def need_money(month, salary, spend, increase):
    money = 0
    for i in range(month):
        money -= salary - spend
        spend *= 1 + increase
    return money

salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

print(round(need_money(months, salary, spend, increase)))
