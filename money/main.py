class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        if 0 <= cents < 100:
            self.cents = cents
        else:
            raise ValueError('Cents should be in range 0-100')

    def __str__(self):
        return f'{self.dollars}.{self.cents}$'

    def __add__(self, another_money):
        total_cents = self.to_cents()
        another_total_cents = another_money.to_cents()
        cents_sum = total_cents + another_total_cents
        return self.from_cents(cents_sum)

    def __sub__(self, another_money):
        total_cents = self.to_cents()
        another_total_cents = another_money.to_cents()
        cents_diff = total_cents - another_total_cents
        return self.from_cents(cents_diff)

    def __truediv__(self, divider):
        total_cents = self.to_cents()
        total_cents /= divider
        return self.from_cents(total_cents)

    def __mul__(self, multiplier):
        total_cents = self.to_cents()
        total_cents *= multiplier
        return self.from_cents(total_cents)

    def __gt__(self, another_money):
        return self.to_cents() > another_money.to_cents()

    def to_cents(self):
        return self.dollars * 100 + self.cents

    @classmethod
    def from_cents(cls, cents):
        dollars = cents // 100
        cents = cents % 100
        return cls(int(dollars), int(cents))


if __name__ == '__main__':
    num = 2
    money = Money(2, 50)
    second_money = Money(2, 60)
    print(f'First value: {money}')
    print(f'Second value: {second_money}')
    print(f'sum = {money + second_money}')
    print(f'diff = {money - second_money}')
    print(f'division = {money / num}')
    print(f'multiply = {money * num}')
    print(f'is first number greater?\n{money < second_money}')
