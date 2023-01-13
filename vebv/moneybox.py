class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return True if v <= self.capacity else False

    def add(self, v):
        self.capacity -= v

    def print_money(self):
        print(100 - self.capacity)

m = MoneyBox(100)

while m.capacity != 0:
    print('Write - "Money", if u want to see your balance')
    v = input()
    if v.lower() == 'money':
        m.print_money()
    elif m.can_add(int(v)) == True:
        m.add(int(v))
    else:
        print(m.can_add(int(v)))
print('MoneyBox is full')