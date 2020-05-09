class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_add(self):
        return self.a + self.b

    def calc_div(self):
        return self.a // self.b


if __name__ == '__main__':
    add = Calc(1, 1)
    print(add.calc_add())