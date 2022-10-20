def need_money(month_def, salary_def, spend_def, increase_def):
    money = 0
    for i in range(month_def):
        money += salary_def - spend_def
        spend_def *= 1 + increase_def
    return -money

salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

print(round(need_money(months, salary, spend, increase)))
