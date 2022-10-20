def time_to_death(money_def, salary_def, spend_def, increase_def):
    month = 0
    spend_money = spend_def
    while True:

        money_def += salary_def - spend_money
        print(money_def)
        spend_money *= 1 + increase_def

        if money_def < 0:
            break
        month += 1
    return month


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
money = money_capital
month = 0

# print(month)

#  Зарплата	Месячная инфляция 	Финансовая подушка	Траты
#   5000	    0,05	            10000	            6000
#
# Месяцы	Деньги на начало месяца	Деньги на конец	траты
# 1	        10000	                9000	        6000
# 2	        9000	                7700	        6300
# 3	        7700	                6085	        6615
# 4	        6085	                4139,25	        6945,75
# 5	        4139,25	                1846,2125	    7293,0375
# 6	        1846,2125	            -811,476875	    7657,689375
# Подсчет сделан в excel -- целых месяцев 5


print(time_to_death(money, salary, spend, increase))
