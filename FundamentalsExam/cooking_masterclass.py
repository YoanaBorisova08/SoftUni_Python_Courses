from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

flour_count = students - (students//5)
egg_count = 10*students
apron_count = ceil(120/100*students)

sum_products = flour_count*flour_price + egg_count*egg_price + apron_count*apron_price
if sum_products <= budget:
    print(f"Items purchased for {sum_products:.2f}$.")
else:
    print(f"{sum_products-budget:.2f}$ more needed.")
