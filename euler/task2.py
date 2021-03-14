# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def is_palindrome(number):
    return str(number) == str(number)[::-1]


max_pal = 0


for i in range(100, 1000):
    for j in range(100, 1000):
        multiplied = i * j
        if is_palindrome(multiplied) and multiplied > max_pal:
            max_pal = multiplied

print(max_pal)
