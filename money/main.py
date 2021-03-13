import math


class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.total_money = self.dollars + self.cents

    def __str__(self):
        return f'{self.total_money}$'

    def __add__(self, another_money):
        sum_dollars = self.dollars + another_money.dollars
        sum_cents = self.cents + another_money.cents
        if sum_cents > 1:
            sum_dollars += 1
            sum_cents -= 1
        return Money(sum_dollars, sum_cents)

    def __sub__(self, another_money):
        diff_dollars = self.dollars - another_money.dollars
        diff_cents = self.cents - another_money.cents
        if diff_cents < 0:
            diff_dollars -= 1
            diff_cents += 1
        return Money(diff_dollars, diff_cents)

    def divide_sum(self, another_money, divider):
        money_sum = self.total_money + another_money.total_money
        sum_divide = money_sum / divider
        return sum_divide

    def divide_diff(self, another_money, divider):
        money_diff = self.total_money - another_money.total_money
        diff_divide = money_diff / divider
        return diff_divide

    def multiply(self, multiplier):
        return self.total_money * multiplier

    def is_greater(self, another_money):
        return self.total_money > another_money.total_money


if __name__ == '__main__':
    num = 2
    money = Money(2, 0.5)
    second_money = Money(2, 0.6)
    print(f'First value: {money}')
    print(f'Second value: {second_money}')
    print(f'sum = {money.__add__(second_money)}')
    print(f'diff = {money.__sub__(second_money)}')
    print(f'division of sum = {money.divide_sum(money, num)}')
    print(f'division of diff = {money.divide_diff(second_money, num)}')
    print(f'multiply = {money.multiply(num)}')
    print(f'is first number greater?\n{money.is_greater(second_money)}')

