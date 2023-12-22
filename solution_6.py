# Задание 6: Внесение изменений в список товаров

products: list[str] = ['Чай', 'Кофе', 'Сахар']

products.insert(1, 'Мёд')
print(f"Товары на полке:", products)
