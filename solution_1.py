# Задание 1: Инвентаризация магазина Романа

products = input('Введите товары через запятую: ')
list_products = products.split(',')
print(f"Товары с нечётными индексами:", ','.join(list_products[1::2]))
