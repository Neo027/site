class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.balance = 0

    def can_add(self, v):
        return True if v <= self.capacity - self.balance else False

    def add(self, v):
        if self.can_add():
            self.balance += v
        else:
            print('insufficient capacity')
    
    def input_add(self):
        try:
            v = int(input())
            self.add(v);
        except ValueError:
            print('incorrect input, try again')

    def print_balance(self):
        print(self.balance)

mb = MoneyBox(100)
mb.input_add()
