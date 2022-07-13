# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Merchandise:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"(Name: {self.name}, Price: {self.price})"

    def __repr__(self):
        return f"(Name: {self.name}, Price: {self.price})"


class VendingMachine:
    commands = ['menu', 'item', 'pay', 'refund', 'exit']
    menu = []
    stock = {}
    collected = {5: 0, 10: 0, 25: 0, 100: 0, 200: 0, 500: 0, 1000: 0, 2000: 0}
    change = {200: 0, 100: 0, 25: 0, 10: 0, 5: 0}
    credit = 0

    def find_item(self, name):
        for i in self.menu:
            if i.name == name:
                return i

    def change_total(self):
        return sum([k*v for k, v in self.change.items()])

    def __init__(self, stock, change):
        self.menu = stock.keys()
        self.stock = stock
        self.change = change

    def healthcheck(self):
        self.show_menu()
        print("Stock:", self.stock)
        print("Credit:", self.credit)
        print("Change:", self.change)
        print("Collected", self.collected_total())

    def collected_total(self):
        return sum([k * v for k, v in self.collected.items()])

    def pay(self, coin):
        try:
            self.collected[coin] += 1
            if coin in self.change.keys():
                self.change[coin] += 1
            self.credit += coin
            print(f"The amount of {coin} has been paid")
            print(f"Total credit is {self.credit}")
        except KeyError:
            print(f'{coin} is not a valid amount')
            print(f"Total credit is {self.credit}")

    def show_menu(self):
        for s in self.menu:
            print(s)

    def serve(self, item):
        if self.stock[item] > 0:
            self.stock[item] -= 1
            self.credit -= item.price
            print(f"Item {item.name} served")
            print(f"Current credit is {self.credit}")
        else:
            print(f"Item {item.name} is not available at the moment")

    def calc_refund(self):
        coins = sorted(self.change.keys(), reverse=True)
        credit = self.credit
        res = {}
        for c in coins:
            noc = min(credit // c, self.change[c])
            if noc > 0:
                res[c] = noc
                credit -= noc * c
                if credit == 0:
                    return res
        print(f"We cannot make the full refund, sorry ah")
        return res

    def refund(self):
        ref = self.calc_refund()
        if ref:
            for k, v in ref.items():
                self.change[k] -= v
                self.collected[k] -= v
            total_refund = sum([k*v for k, v in ref.items()])
            self.credit = self.credit - total_refund
            print(f"Refunded {ref}, total refund {total_refund}")
            print(f"Current credit {self.credit}")

    def run(self):
        self.healthcheck()
        while i := input('>'):
            cmd = i.split()
            if len(cmd) == 1:
                if cmd[0] == 'menu':
                    self.show_menu()
                elif cmd[0] == 'healthcheck':
                    self.healthcheck()
                elif cmd[0] == 'refund':
                    self.refund()
                elif cmd[0] == 'exit':
                    exit(0)
                else:
                    print('Wrong input')
            elif len(cmd) == 2:

                if cmd[0] == 'pay':
                    try:
                        self.pay(int(cmd[1]))
                    except ValueError:
                        print ('Wrong input')
                elif cmd[0] == 'item':
                    item = self.find_item(cmd[1])
                    if item:
                        if self.credit >= item.price:
                            self.serve(item)
                        else:
                            print(item)
                            print(f"Current credit is {self.credit}. Please add {item.price-self.credit} to buy this {item.name}")
                    else:
                        print(f'Item "{cmd[1]}" does not exists')
                else:
                    print('Wrong input')
            else:
                print('Wrong input')


if __name__ == '__main__':
    m1 = Merchandise('Candy', 200)
    m2 = Merchandise('Chips', 150)
    m3 = Merchandise('Soda', 100)
    v = VendingMachine(stock={m1: 10, m2: 10, m3: 20}, change={200: 20, 100: 20, 25: 20, 10: 40, 5: 40})
    v.run()
