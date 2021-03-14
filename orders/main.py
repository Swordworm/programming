class PriceCalculator:
    @staticmethod
    def calculate(products):
        total = sum(product.price for product in products)
        return round(total, 2)


class Product:
    def __init__(self, sku, title, price):
        self.sku = sku
        self.title = title
        self.price = price


class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    @property
    def total_sum(self):
        return PriceCalculator.calculate(self.products)


class Customer:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self.cart = []

    def __str__(self):
        return f'Customer {self.name} ({self.balance})'

    def add_products_to_cart(self, *args):
        self.cart.extend(args)

    def delete_product_from_cart(self, product):
        self.cart.remove(product)

    def checkout(self):
        if PriceCalculator.calculate(self.cart) > self.balance:
            raise ValueError(f'Customer {self.name} doesn\'t have enough money')
        order = Order(self, self.cart.copy())
        self.cart.clear()
        self.balance -= order.total_sum
        return order


if __name__ == '__main__':
    t_shirt = Product(1, 'Nike t-shirt', 90.99)
    jeans = Product(2, 'Puma jeans', 40.00)
    sneakers = Product(3, 'Adidas sneakers', 120.49)

    john = Customer('John', 500.00)
    john.add_products_to_cart(t_shirt, jeans, sneakers)
    # john.add_products_to_cart(jeans)
    # john.add_products_to_cart(sneakers)
    john.delete_product_from_cart(jeans)

    john_order = john.checkout()

    william = Customer('William', 200.00)
    william.add_products_to_cart(t_shirt, jeans, sneakers)
    # william.add_products_to_cart(jeans)
    # william.add_products_to_cart(sneakers)

    print(john_order.total_sum)
    try:
        william.checkout()
    except ValueError as e:
        print('Failed to checkout!', str(e))

    print(william)
    print(john.balance)
