src = not False and True or False and not True
# Избавляемся от логического оператора NOT
result = True and True or False and False
# Избавляемся от логического оператора И
result = True or False
# Избавляемся от логического оператора ИЛИ
result = True

print(src == result)
