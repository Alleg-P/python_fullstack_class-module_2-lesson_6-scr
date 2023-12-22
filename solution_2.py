# Задание 2: Скидки на определенные товары

price = input("Введите цены: ")
list_price = price.split(', ')
print(f"Цены без скидки:", ', '.join(list_price[1::2]))
