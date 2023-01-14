class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.balance = 0

    def can_add(self, v):
        return True if v <= self.capacity - self.balance else False

    def add(self, v):
        if self.can_add(v):
            self.balance += v
            print('Coins in MoneyBox - ', self.balance)
        else:
            print('insufficient capacity')
    
    def input_add(self):
        while self.balance != self.capacity:
            try:
                v = int(input())
                self.add(v)
            except ValueError:
                print('incorrect input, try again')

    def print_balance(self):
        print(self.balance)

mb = MoneyBox(100)
mb.input_add()
print('MoneyBox is full!')