# Задание 5: Обмен цен

price_1 = [10, 30, 40, 50]
price_2 = [5, 10, 15, 25, 20]

i, j = price_1.index(min(price_1)), price_1.index(max(price_1))
price_1[i], price_1[j] = price_1[j], price_1[i]

k, t = price_2.index(min(price_2)), price_2.index(max(price_2))
price_2[k], price_2[t] = price_2[t], price_2[k]

print(price_1)
print(price_2)
