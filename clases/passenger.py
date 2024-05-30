class Passenger:
    def __init__(self, num):
        self.num = num

    def validNumber(self):
        print("this working here")
        return type(self.num) == int and self.num > 0

    def forHereDiscount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num <= 10:
            return 0.2
        else:
            return 0.0
