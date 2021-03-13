import math


class Money:
    def __init__(self, money_quantity):
        self.bills = math.floor(money_quantity)
        self.coins = round(money_quantity - self.bills, 2)
        self.total_money = self.bills + self.coins

    def print(self):
        print(self.bills, self.coins, sep=', ')

    def add(self, another_money):
        money_sum = self.total_money + another_money.total_money
        return money_sum

    def diff(self, another_money):
        money_diff = self.total_money - another_money.total_money
        return money_diff

    def add_divide(self, another_money, divider):
        money_sum = self.total_money + another_money.total_money
        sum_divide = money_sum / divider
        return sum_divide

    def diff_divide(self, another_money, divider):
        money_diff = self.total_money - another_money.total_money
        diff_divide = money_diff / divider
        return diff_divide

    def multiply(self, multiplier):
        return (self.bills + self.coins) * multiplier

    def is_greater(self, another_money):
        return self.total_money > another_money.total_money


if __name__ == '__main__':
    entered_money = 10.7  # float(input('Enter money: '))
    another_entered_money = 15.5   # float(input('Enter second money: '))
    num = 2
    money = Money(entered_money)
    second_money = Money(another_entered_money)
    print(f'sum = {money.add(second_money)}')
    print(f'diff = {money.diff(second_money)}')
    print(f'division of sum = {money.add_divide(second_money, num)}')
    print(f'division of diff = {money.diff_divide(second_money, num)}')
    print(f'multiply = {money.multiply(num)}')
    print(f'is first number greater?\n{money.is_greater(second_money)}')
