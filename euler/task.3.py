# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

num = 0
result = 0
condition = True
while condition:

    for j in range(1, 20):
        if num != 0 and num % j == 0:
            result = num
            condition = False
    num += 1

print(result)
